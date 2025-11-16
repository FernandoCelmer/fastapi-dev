"""
API v1 router.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import item
from app.api.v1.endpoints import templates

api_router = APIRouter()

api_router.include_router(item.router, tags=["Items"], prefix="/items")
api_router.include_router(templates.router, tags=["Templates"])
