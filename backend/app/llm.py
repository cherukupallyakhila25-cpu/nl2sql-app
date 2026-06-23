from openai import OpenAI
from .config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SCHEMA_CONTEXT = """
You are an expert SQL generator for PostgreSQL.

Database schema:
customers(id, name, email, created_at)
orders(id, customer_id, amount, status, created_at)

Rules:
- Only generate SELECT queries
- No INSERT, UPDATE, DELETE
- Always return only SQL
"""

def generate_sql(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SCHEMA_CONTEXT},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content.strip()
