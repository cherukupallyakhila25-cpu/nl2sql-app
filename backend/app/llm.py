from openai import OpenAI
from .config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SCHEMA_CONTEXT = """
You are an expert SQL generator.
Convert natural language into PostgreSQL SQL only.

Database schema:
table: customers(id, name, email, created_at)
table: orders(id, customer_id, amount, status, created_at)

Rules:
- Only generate SELECT queries
- Never use DELETE, UPDATE, INSERT
"""

def generate_sql(natural_language: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SCHEMA_CONTEXT},
            {"role": "user", "content": natural_language}
        ]
    )

    return response.choices[0].message.content.strip()
