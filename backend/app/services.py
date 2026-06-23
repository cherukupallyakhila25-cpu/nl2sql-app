from sqlalchemy import text
from .llm import generate_sql
from .sql_validator import validate_sql


def process_query(db, user_question: str):
    sql = generate_sql(user_question)

    if not validate_sql(sql):
        raise Exception("Unsafe SQL generated")

    result = db.execute(text(sql))
    rows = [dict(row._mapping) for row in result.fetchall()]

    return sql, rows
