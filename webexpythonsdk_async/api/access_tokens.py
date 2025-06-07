"""Webex Access-Tokens API wrapper.

Copyright (c) 2016-2024 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import urllib.parse

import httpx

from ..response_codes import EXPECTED_RESPONSE_CODE
from ..utils import (
    check_response_code,
    check_type,
    dict_from_items_with_values,
    extract_and_parse_json,
    validate_base_url,
)


API_ENDPOINT = "access_token"
OBJECT_TYPE = "access_token"


class AccessTokensAPI:
    """Webex Access-Tokens API.

    Wraps the Webex Access-Tokens API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, base_url, object_factory, single_request_timeout=None):
        """Initialize an AccessTokensAPI object with the provided RestSession.

        Args:
            base_url(str): The base URL the API endpoints.
            single_request_timeout(int): Timeout in seconds for the API
                requests.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(base_url, str)
        check_type(single_request_timeout, int, optional=True)

        self._base_url = str(validate_base_url(base_url))
        self._single_request_timeout = single_request_timeout
        self._endpoint_url = urllib.parse.urljoin(self.base_url, API_ENDPOINT)
        self._request_kwargs = {"timeout": single_request_timeout}

        self._object_factory = object_factory

    @property
    def base_url(self):
        """The base URL the API endpoints."""
        return self._base_url

    @property
    def single_request_timeout(self):
        """Timeout in seconds for the API requests."""
        return self._single_request_timeout

    async def get(self, client_id: str, client_secret: str, code: str, redirect_uri: str):
        """Exchange an Authorization Code for an Access Token.

        Exchange an Authorization Code for an Access Token that can be used to
        invoke the APIs.

        Args:
            client_id(str): Provided when you created your integration.
            client_secret(str): Provided when you created your
                integration.
            code(str): The Authorization Code provided by the user
                OAuth process.
            redirect_uri(str): The redirect URI used in the user OAuth
                process.

        Returns:
            AccessToken: An AccessToken object with the access token provided
            by the Webex cloud.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(client_id, str)
        check_type(client_secret, str)
        check_type(code, str)
        check_type(redirect_uri, str)

        post_data = dict_from_items_with_values(
            grant_type="authorization_code",
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
        )

        # API request
        async with httpx.AsyncClient() as client:
            response = await client.post(self._endpoint_url, data=post_data, **self._request_kwargs)
        check_response_code(response, EXPECTED_RESPONSE_CODE["POST"])
        json_data = extract_and_parse_json(response)

        # Return a access_token object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def refresh(self, client_id, client_secret, refresh_token):
        """Return a refreshed Access Token from the provided refresh_token.

        Args:
            client_id(str): Provided when you created your integration.
            client_secret(str): Provided when you created your
                integration.
            refresh_token(str): Provided when you requested the Access
                Token.

        Returns:
            AccessToken: With the access token provided by the Webex
            cloud.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(client_id, str)
        check_type(client_secret, str)
        check_type(refresh_token, str)

        post_data = dict_from_items_with_values(
            grant_type="refresh_token",
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )

        # API request
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=self._endpoint_url,
                data=post_data,
                **self._request_kwargs,
            )
        check_response_code(response, EXPECTED_RESPONSE_CODE["POST"])
        json_data = extract_and_parse_json(response)

        # Return a AccessToken object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)
