"""
Item endpoints.
"""

from uuid import UUID

from fastapi import APIRouter, Depends
from app.core.auth.security import authorization

router = APIRouter()


@router.get(
    "",
    summary="Get items",
    response_description="List of items"
)
async def get_items(
    _auth=Depends(authorization)
) -> dict[str, str]:
    """Get all items."""
    return {"resource": "item"}


@router.get("/{item_id}", summary="Get item by ID")
async def get_item(
    item_id: UUID,
    _auth=Depends(authorization)
) -> dict[str, str | UUID]:
    """Get a specific item by ID."""
    return {"item_id": item_id, "resource": "item"}
