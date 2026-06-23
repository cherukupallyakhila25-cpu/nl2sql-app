import sqlglot

ALLOWED = {"select"}

def validate_sql(sql: str) -> bool:
    try:
        parsed = sqlglot.parse_one(sql)
        return parsed.key.lower() in ALLOWED
    except Exception:
        return False
