from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from pydantic import BaseModel, Field


class PriceCategory(BaseModel):
    """Price category for the event offer."""

    id: int
    id_at_provider: Optional[str] = Field(None, alias="idAtProvider")
    label: str
    price: int  # Price in cents

    class Config:
        populate_by_name = True


class PriceCategoriesList(BaseModel):
    """
    List of price categories with pagination information.
    """

    priceCategories: List[PriceCategory] = Field(..., alias="data")

    class Config:
        populate_by_name = True
