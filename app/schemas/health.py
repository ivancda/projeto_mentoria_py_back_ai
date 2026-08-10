from pydantic import BaseModel


class ServiceStatus(BaseModel):
    status: str


class HealthResponse(BaseModel):
    status: str
    ollama: ServiceStatus
    db: ServiceStatus
