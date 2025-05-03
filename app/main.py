from fastapi import FastAPI
from app.health import health_router

app = FastAPI()


@app.get("/")
def root(): 
    return { "message" : "Hello autoNote" }

app.add_api_route("/health", health_router)