from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..services import process_query

router = APIRouter()

@router.post("/query")
def query_nl(payload: dict, db: Session = Depends(get_db)):
    user_input = payload["question"]

    results, sql = process_query(db, user_input)

    return {
        "sql": sql,
        "results": results
    }
