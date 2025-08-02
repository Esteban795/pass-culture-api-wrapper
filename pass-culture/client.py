from typing import Optional

import httpx

from .config import Settings
from .endpoints.base import BaseEndpoint
from .endpoints.bookings import BookingsEndpoint
from .exceptions import PassCultureAPIError


class PassCultureClient:
    """
    Async client for the Pass Culture API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_endpoint: Optional[str] = None,
        timeout: int = 30,
    ):
        """
        Initialize the Pass Culture API client.

        Args:
            api_key: API key for authentication
            api_endpoint: Base URL for the API
            timeout: Request timeout in seconds
        """
        self.settings = Settings(
            api_key=api_key,
            api_endpoint=api_endpoint,
        )
        self.timeout = timeout
        self._client = httpx.AsyncClient(
            base_url=self.settings.api_endpoint,
            timeout=self.timeout,
            headers=self._get_default_headers(),
        )
        
        # Initialize endpoints
        self.bookings = BookingsEndpoint(self) 
        
    def _get_default_headers(self) -> dict:
        """
        Get the default headers for API requests.
        """
        return {
            "Authorization": f"Bearer {self.settings.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    
    async def request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json_data: Optional[dict] = None,
    ) -> dict:
        """
        Make an HTTP request to the Pass Culture API.
        """
        try:
            response = await self._client.request(
                method=method,
                url=path,
                params=params,
                data=data,
                json=json_data,
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise PassCultureAPIError(f"HTTP error: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            raise PassCultureAPIError(f"Request error: {str(e)}")
        
    async def close(self):
        """
        Close the underlying HTTP client.
        """
        await self._client.aclose()
        
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()