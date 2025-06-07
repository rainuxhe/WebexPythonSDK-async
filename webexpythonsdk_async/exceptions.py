import logging
import httpx
from .response_codes import RESPONSE_CODES

logger = logging.getLogger(__name__)


class webexpythonsdkException(Exception):
    """Base class for all webexpythonsdk package exceptions."""

    pass


class webexpythonsdkWarning(webexpythonsdkException, Warning):
    """Base class for all webexpythonsdk warnings."""

    pass


class AccessTokenError(webexpythonsdkException):
    """Raised when an incorrect Webex Access Token has been provided."""

    pass


class ApiError(webexpythonsdkException):
    """Errors returned in response to requests sent to the Webex APIs.

    Several data attributes are available for inspection.
    """

    def __init__(self, response: httpx.Response):
        assert isinstance(response, httpx.Response)

        self.response = response
        self.request = self.response.request
        self.status_code = self.response.status_code
        self.status = self.response.reason_phrase
        self.description = RESPONSE_CODES.get(self.status_code)
        self.detail = None

        if "application/json" in self.response.headers.get("Content-Type", "").lower():
            try:
                self.details = self.response.json()
            except ValueError:
                logger.warning("Error parsing JSON response body")

        self.message = self.details.get("message") if self.details else None
        self.tracking_id = (
            self.details.get("trackingId") if self.details else None or self.response.headers.get("trackingId")
        )

        self.error_message = "[{status_code}]{status} - {detail}{tracking_id}".format(
            status_code=self.status_code,
            status=self.status if self.status else "",
            detail=self.message or self.description or "Unknown Error",
            tracking_id=f" [Tracking ID: {self.tracking_id}]" if self.tracking_id else "",
        )
        super().__init__(self.error_message)

    def __repr__(self):
        return "<{exception_name} [{status_code}]{status}>".format(
            exception_name=self.__class__.__name__,
            status_code=self.status_code,
            status=f" {self.status}" if self.status else "",
        )


class ApiWarning(webexpythonsdkWarning, ApiError):
    """Warnings raised from API responses received from the Webex APIs.

    Several data attributes are available for inspection.
    """

    pass


class RateLimitError(ApiError):
    """Webex Rate-Limit exceeded Error.

    Raised when a rate-limit exceeded message is received and the request
    **will not** be retried.
    """

    def __init__(self, response: httpx.Response):
        self.retry_after = max(1, int(response.headers.get("Retry-After", 15)))
        super().__init__(response)


class RateLimitWarning(ApiWarning, RateLimitError):
    """Webex rate-limit exceeded warning.

    Raised when a rate-limit exceeded message is received and the request will
    be retried.
    """

    pass


class MalformedResponse(webexpythonsdkException):
    """Raised when a malformed response is received from Webex."""

    pass
