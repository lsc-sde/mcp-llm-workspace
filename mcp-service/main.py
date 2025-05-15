from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List, Optional

app = FastAPI()


class ContextInput(BaseModel):
    model_id: str
    input: str
    context: Dict[str, str]

class ValidationResponse(BaseModel):
    valid: bool
    missing_fields: List[str]
    message: Optional[str] = None


@app.get("/")
def default_root():
    return {"message": "FastAPI is working."}

@app.post("/validate", response_model=ValidationResponse)
def validate_context(payload: ContextInput):
    required = {"task", "user_role"}
    missing = list(required - payload.context.keys())
    is_valid = len(missing) == 0

    return ValidationResponse(
        valid=is_valid,
        missing_fields=missing,
        message="Valid Context" if is_valid else f"Missing: {', '.join(missing)}"
    ) 