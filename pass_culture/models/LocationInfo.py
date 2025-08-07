from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from pydantic import BaseModel, Field

class LocationInfo(BaseModel):
    """Location information for the event offer."""
    
    type: str  # "physical" or "digital"
    venue_id: Optional[int] = Field(None, alias="venueId")
    
    class Config:
        populate_by_name = True