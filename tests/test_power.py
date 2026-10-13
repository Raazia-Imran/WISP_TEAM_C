import math

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from wisp_team_c.api import app
from wisp_team_c.contracts import PowerRequest
from wisp_team_c.physics import calculate_power, evaluate_limit


def request(**updates):
    data = dict(scenario_id="synthetic-test", source_ids=["TEST-FIXTURE"], basis="scenario",
                intervals=[dict(mean_it_power_kw=10.0, duration_hours=2.0),
                           dict(mean_it_power_kw=4.0, duration_hours=3.0)])
    return PowerRequest(**(data | updates))


def test_weighted_energy_and_cost():
    r = calculate_power(request(repeat_days=2, planning_pue=1.5,
                                tariff_pkr_per_kwh=20.0, carbon_factor_kgco2e_per_kwh=0.5))
    assert r.average_it_power_kw == 6.4
    assert r.it_energy_kwh == 64
    assert r.facility_energy_kwh == 96
    assert r.electricity_cost_pkr == 1920
    assert r.operational_carbon_kgco2e == 48


def test_missing_factor_is_not_zero():
    r = calculate_power(request())
    assert r.facility_energy_kwh is None
    assert r.electricity_cost_pkr is None
    assert evaluate_limit(None, 10.0).status == "UNKNOWN"
    assert evaluate_limit(10.0, 10.0).status == "PASS"
    assert evaluate_limit(10.1, 10.0).status == "FAIL"


@pytest.mark.parametrize("value", [-1.0, math.inf, math.nan])
def test_reject_invalid_power(value):
    with pytest.raises(ValidationError):
        request(intervals=[dict(mean_it_power_kw=value, duration_hours=1.0)])


def test_reject_unknown_fields_and_overlong_day():
    with pytest.raises(ValidationError):
        request(arbitrary_pue=1.4)
    with pytest.raises(ValidationError):
        request(intervals=[dict(mean_it_power_kw=1.0, duration_hours=25.0)])


def test_api_contract():
    client = TestClient(app)
    response = client.post("/api/v1/power/evaluate", json=request().model_dump())
    assert response.status_code == 200
    assert response.json()["it_energy_kwh"] == 32
    assert client.post("/api/v1/power/evaluate", json={}).status_code == 422


def test_explicit_zero_tariff_and_factor_are_valid():
    r = calculate_power(request(planning_pue=1.0, tariff_pkr_per_kwh=0.0,
                                carbon_factor_kgco2e_per_kwh=0.0))
    assert r.electricity_cost_pkr == 0
    assert r.operational_carbon_kgco2e == 0


def test_combined_overflow_is_validation_error():
    data = request(intervals=[dict(mean_it_power_kw=1e308, duration_hours=24.0)])
    response = TestClient(app).post("/api/v1/power/evaluate", json=data.model_dump())
    assert response.status_code == 422


def test_empty_evidence_reference_rejected():
    with pytest.raises(ValidationError):
        request(source_ids=[" "])
