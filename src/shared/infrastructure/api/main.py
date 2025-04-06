from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backoffice.infrastructure.api import routes as backoffice_routes
from src.customer_assistance.infrastructure.api import routes as assistance_routes
from src.shared.infrastructure.deps import initial_setup


@asynccontextmanager
async def lifespan(app: FastAPI):
    initial_setup()
    yield

app = FastAPI(
    title="Landbot Backend Challenge",
    description="API for Landbot Backend Challenge",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assistance_routes.router)
app.include_router(backoffice_routes.router)


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to Landbot Backend Challenge API"}


@app.get("/health")
async def health_check() -> dict:
    return {"status": "healthy"}
