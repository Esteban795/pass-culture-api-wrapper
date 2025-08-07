from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict

from ..models.common import PaginationInfo
from pydantic import BaseModel, Field

from PriceCategory import PriceCategory
from LocationInfo import LocationInfo
from AccessibilityInfo import AccessibilityInfo

class CategoryRelatedFields(BaseModel):
    """Category related fields for the event offer."""
    
    category: str

class EventOfferStatus(str, Enum):
    """Status of an event offer."""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    SOLD_OUT = "SOLD_OUT"


class EventOffer(BaseModel):
    """
    Representation of a Pass Culture Event Offer.
    """
    
    accessibility: AccessibilityInfo
    booking_allowed_datetime: datetime = Field(..., alias="bookingAllowedDatetime")
    booking_contact: Optional[str] = Field(None, alias="bookingContact")
    booking_email: Optional[str] = Field(None, alias="bookingEmail")
    category_related_fields: CategoryRelatedFields = Field(..., alias="categoryRelatedFields")
    description: Optional[str] = None
    enable_double_bookings: bool = Field(..., alias="enableDoubleBookings")
    event_duration: Optional[int] = Field(None, alias="eventDuration")
    external_ticket_office_url: Optional[str] = Field(None, alias="externalTicketOfficeUrl")
    has_ticket: bool = Field(..., alias="hasTicket")
    id: int
    id_at_provider: Optional[str] = Field(None, alias="idAtProvider")
    item_collection_details: Optional[str] = Field(None, alias="itemCollectionDetails")
    location: LocationInfo
    name: str
    price_categories: List[PriceCategory] = Field(..., alias="priceCategories")
    publication_datetime: datetime = Field(..., alias="publicationDatetime")
    status: EventOfferStatus
    
    class Config:
        populate_by_name = True


class EventOfferList(BaseModel):
    """
    List of event offers with pagination information.
    """
    
    event_offers: List[EventOffer] = Field(..., alias="events")
    pagination: PaginationInfo
    
    class Config:
        populate_by_name = True