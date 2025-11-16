"""
This module contains the FastAPI application.
"""

__version__ = "0.1.0"

__author__ = 'Fernando Celmer <fernando-celmer@fernandocelmer.com>'

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1 import api_router as v1_router
from app.core.auth.endpoints import auth
from app.core.settings import settings
from app.core.templates import templates

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
    static_dir = Path("/home") / "static"
    if not static_dir.exists():
        static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        app.mount(
            "/static",
            StaticFiles(directory=str(static_dir)),
            name="static",
        )
    app.include_router(auth, prefix="/auth")
    app.include_router(v1_router, prefix=settings.api_v1_prefix)

    return app
