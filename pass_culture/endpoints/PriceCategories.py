from typing import Optional

from models.common import CtxMessageType
from models.PriceCategory import PriceCategory, PriceCategoriesList
from endpoints.base import BaseEndpoint


class PriceCategoriesEndpoint(BaseEndpoint):
    """
    Endpoint for interacting with Pass Culture price categories.
    """

    priceCategoriesBaseRoute = "offers/v1/events"

    async def get_price_categories(
        self,
        eventId: int,
        limit: Optional[int] = 50,
        firstIndex: Optional[int] = 1,
        idsAtProvider: Optional[str] = None,
    ) -> PriceCategoriesList:
        """
        List price categories for a specific event.

        Args:
            eventId: ID of the event to filter price categories

        Returns:
            PriceCategoriesList object containing the price categories and pagination info
        """

        data = await self._get(
            f"{self.priceCategoriesBaseRoute}/{eventId}/price_categories"
        )
        return PriceCategoriesList.model_validate(data)

    async def create_price_category(
        self, eventId: int, priceCategoriesList: PriceCategoriesList
    ) -> CtxMessageType:
        """
        Create price categories for a specific event.

        Args:
            eventId: ID of the event to create price categories for
            priceCategoriesList: List of PriceCategory objects to create
        Returns:
            CtxMessageType object containing the result of the operation
        """
        params = {
            "priceCategories": [
                pc.model_dump() for pc in priceCategoriesList.price_categories
            ]
        }
        data = await self._post(
            f"{self.priceCategoriesBaseRoute}/{eventId}/price_categories", json=params
        )

        return CtxMessageType.model_validate(data)

    async def update_price_category(
        self, eventId: int, priceCategoryId: int, priceCategory: PriceCategory
    ) -> CtxMessageType:
        """
        Update a specific price category for an event.

        Args:
            eventId: ID of the event to update the price category for
            priceCategoryId: ID of the price category to update
            priceCategory: PriceCategory object with updated details

        Returns:
            CtxMessageType object containing the result of the operation
        """
        params = priceCategory.model_dump()
        data = await self._put(
            f"{self.priceCategoriesBaseRoute}/{eventId}/price_categories/{priceCategoryId}",
            json=params,
        )
        return CtxMessageType.model_validate(data)
