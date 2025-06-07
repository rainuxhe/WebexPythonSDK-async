"""Webex Organizations API wrapper.

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

from webexpythonsdk_async.generator_containers import generator_container
from webexpythonsdk_async.restsession import AsyncRestSession
from webexpythonsdk_async.utils import check_type


API_ENDPOINT = "organizations"
OBJECT_TYPE = "organization"


class OrganizationsAPI(object):
    """Webex Organizations API.

    Wraps the Webex Organizations API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Init a new OrganizationsAPI object with the provided AsyncRestSession.

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
                API calls to the Webex service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, AsyncRestSession)

        super(OrganizationsAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory

    # @generator_container
    async def list(self, **request_parameters):
        """List Organizations.

        Args:
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the organizations returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=request_parameters)

        # # Yield organization objects created from the returned JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=request_parameters):
            yield self._object_factory(OBJECT_TYPE, item)

    async def get(self, orgId):
        """Get the details of an Organization, by ID.

        Args:
            orgId(str): The ID of the Organization to be retrieved.

        Returns:
            Organization: An Organization object with the details of the
            requested organization.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(orgId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + orgId)

        # Return a organization object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)
