native_str = str

import json
import mimetypes
import os
import sys
import urllib.parse
import warnings
from collections import namedtuple, OrderedDict
from datetime import datetime, timedelta, tzinfo


from .config import WEBEX_DATETIME_FORMAT
from .exceptions import (
    ApiError,
    RateLimitError,
)
from .response_codes import RATE_LIMIT_RESPONSE_CODE
import httpx


EncodableFile = namedtuple("EncodableFile", ["file_name", "file_object", "content_type"])


def to_unicode(string):
    """Convert a string (bytes, str or unicode) to unicode."""
    assert isinstance(string, str)
    if sys.version_info[0] >= 3:
        if isinstance(string, bytes):
            return string.decode("utf-8")
        else:
            return string
    else:
        if isinstance(string, str):
            return string.decode("utf-8")
        else:
            return string


def to_bytes(string):
    """Convert a string (bytes, str) to bytes."""
    if isinstance(string, str):
        return string.encode("utf-8")
    elif isinstance(string, bytes):
        return string
    else:
        raise TypeError("'string' must be a string or bytes object; received: {!r}".format(string))


def validate_base_url(base_url):
    """Verify that base_url specifies a protocol and network location."""
    parsed_url = urllib.parse.urlparse(base_url)
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.geturl()
    else:
        error_message = "base_url must contain a valid scheme (protocol specifier) and network location (hostname)"
        raise ValueError(error_message)


def is_web_url(string):
    """Check to see if string is an validly-formatted web url."""
    assert isinstance(string, str)
    parsed_url = urllib.parse.urlparse(string)
    return (parsed_url.scheme.lower() == "http" or parsed_url.scheme.lower() == "https") and parsed_url.netloc


def is_local_file(string):
    """Check to see if string is a valid local file path."""
    assert isinstance(string, str)
    return os.path.isfile(string)


def open_local_file(file_path):
    """Open the file and return an EncodableFile tuple."""
    assert isinstance(file_path, str)
    assert is_local_file(file_path)
    file_name = os.path.basename(file_path)
    file_object = open(file_path, "rb")
    content_type = mimetypes.guess_type(file_name)[0] or "text/plain"
    return EncodableFile(file_name=file_name, file_object=file_object, content_type=content_type)


def check_type(obj, acceptable_types, optional=False):
    """Object is an instance of one of the acceptable types or None.

    Args:
        obj: The object to be inspected.
        acceptable_types: A type or tuple of acceptable types.
        optional(bool): Whether or not the object may be None.

    Returns:
        bool: True if the object is an instance of one of the acceptable types.

    Raises:
        TypeError: If the object is not an instance of one of the acceptable
            types, or if the object is None and optional=False.

    """
    if not isinstance(acceptable_types, tuple):
        acceptable_types = (acceptable_types,)

    if isinstance(obj, acceptable_types):
        # Object is an instance of an acceptable type.
        return True
    elif optional and obj is None:
        # Object is None, and that is OK!
        return True
    else:
        # Object is something else.
        error_message = (
            "We were expecting to receive an instance of one of the following "
            "types: {types}{none}; but instead we received {obj} which is a "
            "{obj_type}.".format(
                types=", ".join([repr(t.__name__) for t in acceptable_types]),
                none="or 'None'" if optional else "",
                obj=obj,
                obj_type=repr(type(obj).__name__),
            )
        )
        raise TypeError(error_message)


def dict_from_items_with_values(*dictionaries, **items):
    """Creates a dict with the inputted items; pruning any that are `None`.

    Args:
        *dictionaries(dict): Dictionaries of items to be pruned and included.
        **items: Items to be pruned and included.

    Returns:
        dict: A dictionary containing all of the items with a 'non-None' value.

    """
    dict_list = list(dictionaries)
    dict_list.append(items)
    result = {}
    for d in dict_list:
        for key, value in d.items():
            if value is not None:
                result[key] = value
    return result


def raise_if_extra_kwargs(kwargs):
    """Raise a TypeError if kwargs is not empty."""
    if kwargs:
        raise TypeError("Unexpected **kwargs: {!r}".format(kwargs))


def check_response_code(response: httpx.Response, expected_response_code: int):
    """Check response code against the expected code; raise ApiError.

    Checks the httpx.response.status_code against the provided expected
    response code (erc), and raises a ApiError if they do not match.

    Args:
        response(httpx.response): The response object returned by a request
            using the httpx package.
        expected_response_code(int): The expected response code (HTTP response
            code).

    Raises:
        ApiError: If the httpx.response.status_code does not match the
            provided expected response code (erc).

    """
    if response.status_code == expected_response_code:
        pass
    elif response.status_code == RATE_LIMIT_RESPONSE_CODE:
        raise RateLimitError(response)
    else:
        raise ApiError(response)


def extract_and_parse_json(response):
    """Extract and parse the JSON data from an httpx.response object.

    Args:
        response(httpx.response): The response object returned by a request
            using the httpx package.

    Returns:
        The parsed JSON data as the appropriate native Python data type.

    """
    return json.loads(response.text, object_hook=OrderedDict)


def json_dict(json_data):
    """Given a dictionary or JSON string; return a dictionary.

    Args:
        json_data(dict, str): Input JSON object.

    Returns:
        A Python dictionary with the contents of the JSON object.

    Raises:
        TypeError: If the input object is not a dictionary or string.

    """
    if isinstance(json_data, dict):
        return json_data
    elif isinstance(json_data, str):
        return json.loads(json_data, object_hook=OrderedDict)
    else:
        raise TypeError("'json_data' must be a dictionary or valid JSON string; received: {!r}".format(json_data))


def make_attachment(card):
    """Given a card, makes a card attachment by attaching the correct
     content type and content.

    Args:
      card(AdaptiveCard): Adaptive Card object that should be attached

    Returns:
      A Python dictionary containing the card attachment dictionary
    """
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": card.to_dict(),
    }

    return attachment


class ZuluTimeZone(tzinfo):
    """Zulu Time Zone."""

    def tzname(self, dt):
        """Time Zone Name."""
        # The future package's newstr is messing with Python2 compatibility
        return native_str("Z")

    def utcoffset(self, dt):
        """UTC Offset."""
        return timedelta(0)

    def dst(self, dt):
        """Daylight Savings Time Offset."""
        return timedelta(0)


class WebexDateTime(datetime):
    """Webex formatted Python datetime."""

    @classmethod
    def strptime(cls, date_string, format=WEBEX_DATETIME_FORMAT):
        """strptime with the Webex DateTime format as the default."""
        return super(WebexDateTime, cls).strptime(date_string, format).replace(tzinfo=ZuluTimeZone())

    def strftime(self, fmt=WEBEX_DATETIME_FORMAT):
        """strftime with the Webex DateTime format as the default."""
        return super(WebexDateTime, self).strftime(fmt)

    def __str__(self):
        """Human readable string representation of this WebexDateTime."""
        if self.tzinfo:
            dt = self.astimezone(ZuluTimeZone())
        else:
            warnings.warn(
                "Datetime {} does not have an associated timezone; assuming it should be UTC/Zulu.".format(repr(self)),
                category=UserWarning,
                stacklevel=2,
            )
            dt = self.replace(tzinfo=ZuluTimeZone())

        return dt.strftime("%Y-%m-%dT%H:%M:%S.{:0=3}%Z").format(self.microsecond // 1000)
