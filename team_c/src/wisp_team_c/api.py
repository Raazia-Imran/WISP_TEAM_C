"""Stateless starter API. Persistence and seven-engine orchestration are planned."""

from fastapi import FastAPI, HTTPException

from .contracts import PowerRequest, PowerResponse
from .physics import calculate_power

app = FastAPI(title="WISP Team C", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "persistence": "not_connected"}


@app.post("/api/v1/power/evaluate", response_model=PowerResponse)
def power(request: PowerRequest):
    try:
        return calculate_power(request)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
