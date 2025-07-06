import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, field_validator

# Load environment variables from .env file
load_dotenv()


class Settings(BaseModel):
    """
    Configuration settings for the Pass Culture API client.
    """
    
    api_key: str
    api_endpoint: str
    
    @field_validator("api_key", mode="before")
    def validate_api_key(cls, v: Optional[str]) -> str:
        """Validate and retrieve API key."""
        if not v:
            v = os.getenv("API_KEY", "")
        if not v:
            raise ValueError("API key is required. Set it via API_KEY environment variable or pass it to the client.")
        return v
    
    @field_validator("api_endpoint", mode="before")
    def validate_api_endpoint(cls, v: Optional[str]) -> str:
        """Validate and retrieve API endpoint."""
        if not v:
            v = os.getenv("API_ENDPOINT", "")
        if not v:
            raise ValueError(
                "API endpoint is required. Set it via API_ENDPOINT environment variable or pass it to the client."
            )
        return v