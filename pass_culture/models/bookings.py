from datetime import datetime
from enum import Enum
from typing import List, Optional

from models.common import PaginationInfo
from pydantic import BaseModel, Field


class BookingStatus(str, Enum):
    """Status of a booking."""
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    USED = "USED"
    REIMBURSED = "REIMBURSED"


class Booking(BaseModel):
    """
    Representation of a Pass Culture booking as per API documentation.
    """
    confirmation_date: Optional[str] = Field(None, alias="confirmationDate")
    creation_date: Optional[str] = Field(None, alias="creationDate")
    id: int
    offer_ean: Optional[str] = Field(None, alias="offerEan")
    offer_id: int = Field(..., alias="offerId")
    offer_name: str = Field(..., alias="offerName")
    price: float
    price_category_id: Optional[int] = Field(None, alias="priceCategoryId")
    price_category_label: Optional[str] = Field(None, alias="priceCategoryLabel")
    quantity: int
    status: BookingStatus
    stock_id: int = Field(..., alias="stockId")
    user_birth_date: Optional[str] = Field(None, alias="userBirthDate")
    user_email: Optional[str] = Field(None, alias="userEmail")
    user_first_name: Optional[str] = Field(None, alias="userFirstName")
    user_last_name: Optional[str] = Field(None, alias="userLastName")
    user_phone_number: Optional[str] = Field(None, alias="userPhoneNumber")
    user_postal_code: Optional[str] = Field(None, alias="userPostalCode")
    venue_address: Optional[str] = Field(None, alias="venueAddress")
    venue_departement_code: Optional[str] = Field(None, alias="venueDepartementCode")
    venue_id: int = Field(..., alias="venueId")
    venue_name: str = Field(..., alias="venueName")
    
    class Config:
        populate_by_name = True

class BookingList(BaseModel):
    """
    List of bookings with pagination information.
    """
    
    bookings: List[Booking] = Field(..., alias="data")
    
    class Config:
        populate_by_name = True