from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import QueryRequest, QueryResponse
from ..services import process_query

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_nl(payload: QueryRequest, db: Session = Depends(get_db)):
    try:
        sql, results = process_query(db, payload.question)

        return {
            "sql": sql,
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
