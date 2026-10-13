"""Pure functions for reviewed dimensional relationships, with explicit inputs."""

from math import isfinite

from .contracts import LimitCheck, PowerRequest, PowerResponse


def evaluate_limit(observed: float | None, limit: float | None) -> LimitCheck:
    if observed is None or limit is None:
        return LimitCheck(status="UNKNOWN", observed=observed, limit=limit,
                          reason="Missing observed value or applicable limit")
    return LimitCheck(status="PASS" if observed <= limit else "FAIL",
                      observed=observed, limit=limit,
                      reason="Compare values using the same unit and boundary")


def calculate_power(request: PowerRequest) -> PowerResponse:
    hours = sum(i.duration_hours for i in request.intervals)
    day_energy = sum(i.mean_it_power_kw * i.duration_hours for i in request.intervals)
    it_energy = day_energy * request.repeat_days
    facility = None if request.planning_pue is None else it_energy * request.planning_pue
    cost = (None if facility is None or request.tariff_pkr_per_kwh is None
            else facility * request.tariff_pkr_per_kwh)
    carbon = (None if facility is None or request.carbon_factor_kgco2e_per_kwh is None
              else facility * request.carbon_factor_kgco2e_per_kwh)
    values = (day_energy, it_energy, facility, cost, carbon)
    if any(v is not None and not isfinite(v) for v in values):
        raise ValueError("Input combination exceeds finite numeric range")
    warnings = [
        "Maximum interval mean is not measured instantaneous peak or electrical design capacity.",
        "PUE is a supplied scenario factor; cooling and UPS losses must not be added again.",
        "Source identifiers are recorded; their evidence is not automatically verified.",
    ]
    if hours < 24:
        warnings.append("Energy covers supplied hours only; unsupplied hours are not assumed idle.")
    if request.repeat_days > 1:
        warnings.append("Repeated profile is a projection, not a measured annual energy total.")
    if facility is None:
        warnings.append(
            "Facility energy, electricity cost and carbon need a supplied planning PUE."
        )
    return PowerResponse(
        scenario_id=request.scenario_id, basis=request.basis, source_ids=request.source_ids,
        covered_hours_per_day=hours, average_it_power_kw=day_energy / hours,
        maximum_interval_mean_it_power_kw=max(i.mean_it_power_kw for i in request.intervals),
        it_energy_kwh=it_energy, facility_energy_kwh=facility,
        electricity_cost_pkr=cost, operational_carbon_kgco2e=carbon,
        warnings=warnings,
        formula_ids=["F-ENE-001", "F-ENE-002", "F-ENE-004"]
        + (["F-FAC-001"] if facility is not None else []),
    )
