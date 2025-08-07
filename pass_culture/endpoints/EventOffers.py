from typing import Optional

from models.common import CtxMessageType
from models.EventOffers import EventOffer,EventOfferList
from endpoints.base import BaseEndpoint


class EventOffersEndpoint(BaseEndpoint):
    """
    Endpoint for interacting with Pass Culture Event Offers.
    """

    eventOffersBaseRoute = "offers/v1"
    
    async def get_event_offers(
        self,
        venueId : int,
        limit : Optional[int] = 50,
        firstIndex : Optional[int] = 1,
        idsAtProvider : Optional[str] = None,
        addressId : Optional[int] = None,
    ) -> EventOfferList:
        """
        List event offers with optional filtering.

        Args:
            offerId: ID of the offer to filter event offers
            firstIndex: Index for pagination (default is 1)
            idsAtProvider: Optional IDs at provider to filter event offers
            addressId: Optional address ID to filter event offers
            
        Returns:
            EventOfferList object containing the event offers and pagination info
        """
        params = {"venueId": venueId, 
                  "firstIndex": firstIndex,
                  "limit": limit,
                  "idsAtProvider": idsAtProvider,
                  "addressId": addressId}      
        data = await self._get(f"{self.eventOffersBaseRoute}/events", params=params)
        return EventOfferList.model_validate(data)

    async def get_event_offer(self, event_offer_id: int) -> EventOffer:
        """
        Get details of a specific event offer.
        
        Args:
            event_offer_id: ID of the event offer to retrieve

        Returns:
            EventOffer object with the details
        """
        data = await self._get(f"{self.eventOffersBaseRoute}/events/{event_offer_id}")
        return EventOffer.model_validate(data)

    async def create_event_offer(self, event_offer_id: int) -> CtxMessageType:
        """
        Cancel an existing event offer.
        
        Args:
            booking_id: ID of the event offer to cancel
            
        Returns:
            Updated EventOffer object
        """
        data = await self._patch(f"{self.eventOffersBaseRoute}/cancel/token/{event_offer_id}")
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