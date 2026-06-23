from .llm import generate_sql
from .sql_validator import validate_sql
from sqlalchemy import text

def process_query(db, user_input: str):
    sql = generate_sql(user_input)

    if not validate_sql(sql):
        raise Exception("Unsafe or invalid SQL generated")

    result = db.execute(text(sql))
    return [dict(row) for row in result.fetchall()], sql
