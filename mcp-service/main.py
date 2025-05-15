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