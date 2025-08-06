from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PaginationInfo(BaseModel):
    """Pagination information."""
    
    total: int
    page: int
    limit: int
    pages: int


class CtxMessageType(BaseModel):
    """
    Context message type for API error responses.
    """
    
    ctx: Dict[str, Any] = Field(default_factory=dict)
    loc: List[str]
    msg: str
    type: str