from fastapi import FastAPI
from . import models
from .db import engine, Base
from .routes import router as tasks_router

app = FastAPI(title="ToDo App - FastAPI + Postgres")

Base.metadata.create_all(bind=engine)

app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI ToDo (Postgres). See /docs for API docs."}
