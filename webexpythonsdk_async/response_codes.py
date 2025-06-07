RESPONSE_CODES = {
    200: "Successful request with body content.",
    204: "Successful request without body content.",
    400: "The request was invalid or cannot be otherwise served.",
    401: "Authentication credentials were missing or incorrect.",
    403: "The request is understood, but it has been refused or access is not allowed.",
    404: "The URI requested is invalid or the resource requested, such as a "
    "user, does not exist. Also returned when the requested format is "
    "not supported by the requested method.",
    405: "The request was made to a resource using an HTTP request method that is not supported.",
    409: "The request could not be processed because it conflicts with some "
    "established rule of the system. For example, a person may not be "
    "added to a room more than once.",
    410: "The requested resource is no longer available.",
    415: "The request was made to a resource without specifying a media type "
    "or used a media type that is not supported.",
    423: "The requested resource is temporarily unavailable. A `Retry-After` "
    "header may be present that specifies how many seconds you need to "
    "wait before attempting the request again.",
    429: "Too many requests have been sent in a given amount of time and the "
    "request has been rate limited. A `Retry-After` header should be "
    "present that specifies how many seconds you need to wait before a "
    "successful request can be made.",
    500: "Something went wrong on the server. If the issue persists, feel "
    "free to contact the Webex Developer Support team "
    "(https://developer.webex.com/support).",
    502: "The server received an invalid response from an upstream server "
    "while processing the request. Try again later.",
    503: "Server is overloaded with requests. Try again later.",
}

RATE_LIMIT_RESPONSE_CODE = 429

EXPECTED_RESPONSE_CODE = {"GET": 200, "POST": 200, "PUT": 200, "DELETE": 204}
