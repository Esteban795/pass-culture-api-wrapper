class PassCultureAPIError(Exception):
    """Base exception for all Pass Culture API errors."""
    pass


class AuthenticationError(PassCultureAPIError):
    """Raised when authentication fails."""
    pass


class RateLimitError(PassCultureAPIError):
    """Raised when the API rate limit is exceeded."""
    pass


class ResourceNotFoundError(PassCultureAPIError):
    """Raised when a requested resource is not found."""
    pass