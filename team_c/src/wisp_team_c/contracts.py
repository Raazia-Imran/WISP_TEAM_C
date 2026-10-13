"""Versioned API models. Units are encoded in field names."""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

NonNegative = Annotated[float, Field(ge=0)]
Positive = Annotated[float, Field(gt=0)]


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class PowerInterval(Contract):
    mean_it_power_kw: NonNegative
    duration_hours: Positive


class PowerRequest(Contract):
    schema_version: Literal["1.0"] = "1.0"
    scenario_id: Annotated[str, Field(min_length=1, max_length=100)]
    source_ids: Annotated[list[str], Field(min_length=1)]
    basis: Literal["measured", "calibrated", "scenario"]
    intervals: Annotated[list[PowerInterval], Field(min_length=1, max_length=8760)]
    repeat_days: Annotated[int, Field(ge=1, le=366)] = 1
    planning_pue: Annotated[float, Field(ge=1)] | None = None
    tariff_pkr_per_kwh: NonNegative | None = None
    carbon_factor_kgco2e_per_kwh: NonNegative | None = None

    @model_validator(mode="after")
    def validate_day(self):
        if sum(i.duration_hours for i in self.intervals) > 24:
            raise ValueError("A repeated profile must cover at most 24 hours")
        if any(not x.strip() for x in self.source_ids):
            raise ValueError("source_ids must contain nonblank evidence references")
        return self


class PowerResponse(Contract):
    schema_version: Literal["1.0"] = "1.0"
    scenario_id: str
    basis: Literal["measured", "calibrated", "scenario"]
    source_ids: list[str]
    covered_hours_per_day: Positive
    average_it_power_kw: NonNegative
    maximum_interval_mean_it_power_kw: NonNegative
    it_energy_kwh: NonNegative
    facility_energy_kwh: NonNegative | None
    electricity_cost_pkr: NonNegative | None
    operational_carbon_kgco2e: NonNegative | None
    warnings: list[str]
    formula_ids: list[str]


class LimitCheck(Contract):
    status: Literal["PASS", "FAIL", "UNKNOWN"]
    observed: NonNegative | None
    limit: NonNegative | None
    reason: str
