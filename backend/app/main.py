from fastapi import FastAPI
from .routers import query
from .db import Base, engine

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NL2SQL System")

app.include_router(query.router)


@app.get("/")
def root():
    return {"message": "NL2SQL API is running"}
