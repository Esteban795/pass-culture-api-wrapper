from typing import Any, Dict, Optional


class BaseEndpoint:
    """
    Base class for API endpoints.
    """
    
    def __init__(self, client):
        self.client = client
        
    async def _get(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a GET request to the API.
        """
        return await self.client.request("GET", path, params=params)
    
    async def _post(
        self, path: str, json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a POST request to the API.
        """
        return await self.client.request("POST", path, json_data=json_data)
    
    async def _patch(
        self, path: str, json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a PATCH request to the API.
        """
        return await self.client.request("PATCH", path, json_data=json_data
    )