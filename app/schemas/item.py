"""
This module contains the item schemas.
"""

from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    """Base schema for the item."""
    title: str
    description: str
    status: bool = True


class SchemaPatch(BaseModel):
    """Patch schema for the item."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: bool = None


class SchemaCreate(SchemaBase):
    """Create schema for the item."""
    pass


class Schema(SchemaBase):
    """Schema for the item."""
    id: int

    class Config:
        """Config for the item."""
        from_attributes = False
