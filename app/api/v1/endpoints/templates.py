"""
Template endpoints.
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.templates import templates

router = APIRouter()
@router.get(
    "/",
    response_class=HTMLResponse,
    summary="Home page",
    tags=["Templates"]
)
async def home(request: Request) -> HTMLResponse:
    """Render the home page template."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "project_name": "FastAPI Template",
        },
    )
