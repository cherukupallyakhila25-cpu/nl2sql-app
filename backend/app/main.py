from fastapi import FastAPI
from .routers import query

app = FastAPI(title="NL2SQL API")

app.include_router(query.router)

@app.get("/")
def health():
    return {"status": "running"}
