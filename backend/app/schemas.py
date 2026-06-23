from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    sql: str
    results: List[dict]
