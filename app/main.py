from fastapi import FastAPI

from app import models
from app.database import engine
from app.routes import users, todos

app = FastAPI(title="Todo API")
app.include_router(users.router)
models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(todos.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Todo API 🚀"}
