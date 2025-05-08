from fastapi import FastAPI
from app.health import health_router
from app.routes.notes import notes_router
from app.database import init_db, engine
from contextlib import asynccontextmanager
from fastapi.security.api_key import APIKeyHeader
from fastapi.openapi.utils import get_openapi

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="AutoNote",
        version="1.0.0",
        description="API sécurisée par clé API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "in": "header",
            "name": "x-api-key"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_engine = engine
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.openapi = custom_openapi


@app.get("/")
def root():
    return {"message": "Hello autoNote"}


app.add_api_route("/health", health_router)
app.include_router(notes_router)