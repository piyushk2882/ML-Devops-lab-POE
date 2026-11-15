from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from add import add_numbers

app = FastAPI(title="Addition API")

# In-memory demo history. It resets whenever the app restarts.
_observations: list[dict[str, float]] = []


class AdditionRequest(BaseModel):
    a: float
    b: float


@app.post("/add")
def add(request: AdditionRequest) -> dict[str, float]:
    result = add_numbers(request.a, request.b)
    _observations.append({"a": request.a, "b": request.b, "sum": result})
    return {"a": request.a, "b": request.b, "result": result}


@app.get("/evidently-report")
def evidently_report() -> dict[str, object]:
    """Compare the first half of observed requests with the second half."""
    if len(_observations) < 2:
        raise HTTPException(
            status_code=400,
            detail="Send at least two requests to /add before creating a report.",
        )

    import pandas as pd
    from evidently import Report
    from evidently.presets import DataDriftPreset

    split_at = len(_observations) // 2
    reference = pd.DataFrame(_observations[:split_at])
    current = pd.DataFrame(_observations[split_at:])
    evaluation = Report([DataDriftPreset()]).run(
        current_data=current,
        reference_data=reference,
    )
    return evaluation.dict()
