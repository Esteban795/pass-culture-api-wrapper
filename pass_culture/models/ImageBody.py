from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from pydantic import BaseModel, Field


class ImageBody(BaseModel):

    credit: Optional[str] = Field(None, description="Credit for the image")
    file: Optional[str] = Field(
        None,
        description="Image file encoded in base64 string. Image format must be PNG or JPEG. Size must be between 400x600 and 800x1200 pixels. Aspect ratio must be 2:3 (portrait format).",
    )
