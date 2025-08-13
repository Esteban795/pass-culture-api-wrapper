from typing import Optional

from models.common import CtxMessageType
from models.EventOffers import EventOffer, EventOfferList
from models.AccessibilityInfo import AccessibilityInfo
from models.CategoryRelatedFields import CategoryRelatedFields
from models.LocationInfo import LocationInfo
from models.PriceCategory import PriceCategory
from models.ImageBody import ImageBody
from endpoints.base import BaseEndpoint


class EventOffersEndpoint(BaseEndpoint):
    """
    Endpoint for interacting with Pass Culture Event Offers.
    """

    eventOffersBaseRoute = "offers/v1"

    async def get_event_offers(
        self,
        venueId: int,
        limit: Optional[int] = 50,
        firstIndex: Optional[int] = 1,
        idsAtProvider: Optional[str] = None,
        addressId: Optional[int] = None,
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
        params = {
            "venueId": venueId,
            "firstIndex": firstIndex,
            "limit": limit,
            "idsAtProvider": idsAtProvider,
            "addressId": addressId,
        }
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

    async def create_event_offer(
        self,
        accessibility: AccessibilityInfo,
        categoryRelatedField: CategoryRelatedFields,
        hasTicket: bool,
        location: LocationInfo,
        name: str,
        bookingAllowedDateTime: Optional[str] = None,
        bookingContact: Optional[str] = None,
        bookingEmail: Optional[str] = None,
        description: Optional[str] = None,
        enableDoubleBooking: Optional[bool] = True,
        eventDuration: Optional[int] = None,
        externalTicketOfficeUrl: Optional[str] = None,
        idAtProvider: Optional[str] = None,
        image: ImageBody = None,
        itemCollectionDetails: Optional[str] = None,
        priceCategories: Optional[list[PriceCategory]] = None,
        publicationDate: Optional[str] = None,
    ) -> CtxMessageType:
        """
        Create an event offer.

        Args:
            booking_id: ID of the event offer to cancel

        Returns:
            Updated EventOffer object
        """
        params = {
            "accessibility": accessibility.model_dump(),
            "categoryRelatedField": categoryRelatedField.model_dump(),
            "hasTicket": hasTicket,
            "location": location.model_dump(),
            "name": name,
            "bookingAllowedDateTime": bookingAllowedDateTime,
            "bookingContact": bookingContact,
            "bookingEmail": bookingEmail,
            "description": description,
            "enableDoubleBooking": enableDoubleBooking,
            "eventDuration": eventDuration,
            "externalTicketOfficeUrl": externalTicketOfficeUrl,
            "idAtProvider": idAtProvider,
            "image": image.model_dump() if image else None,
            "itemCollectionDetails": itemCollectionDetails,
            "priceCategories": (
                [pc.model_dump() for pc in priceCategories] if priceCategories else None
            ),
            "publicationDate": publicationDate,
        }
        data = await self._post(f"{self.eventOffersBaseRoute}/events", json=params)
        return CtxMessageType.model_validate(data)

    async def update_event_offer(
        self,
        accessibility: AccessibilityInfo,
        categoryRelatedField: CategoryRelatedFields,
        hasTicket: bool,
        location: LocationInfo,
        name: str,
        bookingAllowedDateTime: Optional[str] = None,
        bookingContact: Optional[str] = None,
        bookingEmail: Optional[str] = None,
        description: Optional[str] = None,
        enableDoubleBooking: Optional[bool] = True,
        eventDuration: Optional[int] = None,
        externalTicketOfficeUrl: Optional[str] = None,
        idAtProvider: Optional[str] = None,
        image: ImageBody = None,
        itemCollectionDetails: Optional[str] = None,
        priceCategories: Optional[list[PriceCategory]] = None,
        publicationDate: Optional[str] = None,
    ) -> CtxMessageType:
        """
        Update an existing event offer.

        Args:
            booking_id: ID of the event offer to cancel

        Returns:
            Updated EventOffer object
        """
        params = {
            "accessibility": accessibility.model_dump(),
            "categoryRelatedField": categoryRelatedField.model_dump(),
            "hasTicket": hasTicket,
            "location": location.model_dump(),
            "name": name,
            "bookingAllowedDateTime": bookingAllowedDateTime,
            "bookingContact": bookingContact,
            "bookingEmail": bookingEmail,
            "description": description,
            "enableDoubleBooking": enableDoubleBooking,
            "eventDuration": eventDuration,
            "externalTicketOfficeUrl": externalTicketOfficeUrl,
            "idAtProvider": idAtProvider,
            "image": image.model_dump() if image else None,
            "itemCollectionDetails": itemCollectionDetails,
            "priceCategories": (
                [pc.model_dump() for pc in priceCategories] if priceCategories else None
            ),
            "publicationDate": publicationDate,
        }
        data = await self._patch(f"{self.eventOffersBaseRoute}/events", json=params)
        return CtxMessageType.model_validate(data)
