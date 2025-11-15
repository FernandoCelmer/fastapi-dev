"""
This module contains the FastAPI application.
"""

__version__ = "0.1.0"

__author__ = "Fernando Celmer <fernando-celmer@fernandocelmer.com>"


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router as v1_router
from app.core.auth.endpoints import auth
from app.core.settings import settings

app = FastAPI(
    title="FastAPI Template",
    description="Amazing project with FastAPI!",
    version=__version__,
    debug=settings.is_development,
)


def create_app() -> FastAPI:
    """Create the FastAPI application."""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(auth, prefix="/auth")
    app.include_router(v1_router, prefix=settings.api_v1_prefix)

    return app
