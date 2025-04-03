from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.customer_assistance.infrastructure.api import routes as assistance_routes

app = FastAPI(
    title="Landbot Backend Challenge",
    description="API for Landbot Backend Challenge",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assistance_routes.router)


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to Landbot Backend Challenge API"}


@app.get("/health")
async def health_check() -> dict:
    return {"status": "healthy"}
