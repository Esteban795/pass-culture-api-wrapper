from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from pydantic import BaseModel, Field

class AccessibilityInfo(BaseModel):
    """Accessibility compliance information."""
    
    audio_disability_compliant: bool = Field(..., alias="audioDisabilityCompliant")
    mental_disability_compliant: bool = Field(..., alias="mentalDisabilityCompliant")
    motor_disability_compliant: bool = Field(..., alias="motorDisabilityCompliant")
    visual_disability_compliant: bool = Field(..., alias="visualDisabilityCompliant")
    
    class Config:
        populate_by_name = True