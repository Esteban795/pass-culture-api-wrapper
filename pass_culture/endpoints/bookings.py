from typing import Optional

from models.common import CtxMessageType
from models.bookings import Booking, BookingList,BookingStatus
from endpoints.base import BaseEndpoint



class BookingsEndpoint(BaseEndpoint):
    """
    Endpoint for interacting with Pass Culture bookings.
    """
    
    bookingsBaseRoute = "bookings/v1"
    
    async def list_bookings(
        self, 
        offerId : int,
        firstIndex : Optional[int] = 1,
        priceCategoryId: Optional[int] = None,
        stockId: Optional[int] = None,
        status : Optional[BookingStatus] = None,
        beginningDatetime : Optional[str] = None
    ) -> BookingList:
        """
        List bookings with optional filtering.
        
        Args:
            offerId: ID of the offer to filter bookings
            firstIndex: Index for pagination (default is 1)
            priceCategoryId: Optional price category ID to filter bookings
            stockId: Optional stock ID to filter bookings
            status: Optional booking status to filter by (BookingStatus enum)
            beginningDatetime: Optional datetime to filter bookings that start after this date. The expected format is ISO 8601 (standard format for timezone aware datetime). 
            
        Returns:
            BookingList object containing the bookings and pagination info
        """
        params = {"offerId": offerId, "firstIndex": firstIndex}
        if priceCategoryId:
            params["priceCategoryId"] = priceCategoryId
        if stockId:
            params["stockId"] = stockId
        if status:
            params["status"] = status.value if isinstance(status, BookingStatus) else status
        if beginningDatetime:   
            params["beginningDatetime"] = beginningDatetime
            
        data = await self._get("bookings/v1/bookings", params=params)
        return BookingList.model_validate(data)
    
    async def get_booking(self, booking_id: int) -> Booking:
        """
        Get details of a specific booking.
        
        Args:
            booking_id: ID of the booking to retrieve
            
        Returns:
            Booking object with the details
        """
        data = await self._get(f"bookings/v1/token/{booking_id}")
        return Booking.model_validate(data)
    
    async def delete_booking(self, booking_id: int) -> CtxMessageType:
        """
        Cancel an existing booking.
        
        Args:
            booking_id: ID of the booking to cancel
            
        Returns:
            Updated Booking object
        """
        data = await self._patch(f"bookings/v1/cancel/token/{booking_id}")
        return CtxMessageType.model_validate(data)
    
    async def validate_booking(self, booking_id: str) -> CtxMessageType:
        """
        Validate a booking (e.g., when the user attends the event).
        
        Args:
            booking_id: ID of the booking to validate
            validation_token: Token required for validation
            
        Returns:
            Updated Booking object
        """
        data = await self._patch(
            f"bookings/v1/use/token/{booking_id}",
        )
        return CtxMessageType.model_validate(data)
    
    async def revert_validation(self, booking_id: int) -> CtxMessageType:
        """
        Revert the validation of a booking.
        
        Args:
            booking_id: ID of the booking to revert
            
        Returns:
            Updated Booking object
        """
        data = await self._patch(f"bookings/v1/keep/token/{booking_id}")
        return CtxMessageType.model_validate(data)