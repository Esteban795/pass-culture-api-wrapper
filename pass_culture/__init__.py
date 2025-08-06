from client import PassCultureClient
from exceptions import PassCultureAPIError, AuthenticationError, RateLimitError, ResourceNotFoundError

__all__ = [
    "PassCultureClient",
    "PassCultureAPIError",
    "AuthenticationError",
    "RateLimitError",
    "ResourceNotFoundError",
]

import dotenv
import asyncio

async def main(client   : PassCultureClient):
    balec = await client.bookings.validate_booking("TNUJTH")
    
    print(balec)

if __name__ == "__main__":
    dotenv.load_dotenv()
    api_key = dotenv.get_key(dotenv.find_dotenv(), "API_TEST_KEY")
    endpoint = dotenv.get_key(dotenv.find_dotenv(), "API_TEST_ENDPOINT")
    client = PassCultureClient(api_key=api_key, api_endpoint=endpoint)
    asyncio.run(main(client))