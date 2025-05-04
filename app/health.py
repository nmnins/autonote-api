
from fastapi_health import health

def is_healthy():
    return True

# Le router à exporter
health_router = health([is_healthy])
