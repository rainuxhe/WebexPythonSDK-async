from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)
# from typing import AsyncGenerator


API_ENDPOINT = "licenses"
OBJECT_TYPE = "license"


class LicensesAPI:
    """Webex Licenses API.

    Wraps the Webex Licenses API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new LicensesAPI object with the provided AsyncRestSession.

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
                API calls to the Webex service.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        check_type(session, AsyncRestSession)

        self._session = session
        self._object_factory = object_factory

    # @generator_container
    async def list(self, orgId=None, **request_parameters):
        """List all licenses for a given organization.

        If no orgId is specified, the default is the organization of the
        authenticated user.

        Args:
            orgId(str): Specify the organization, by ID.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the licenses returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(orgId, str, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
        )

        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=params)

        # # Yield license objects created from the returned JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in generator_container(self.get_items, params):
            yield self._object_factory(OBJECT_TYPE, item)

    async def get(self, licenseId):
        """Get the details of a License, by ID.

        Args:
            licenseId(str): The ID of the License to be retrieved.

        Returns:
            License: A License object with the details of the requested
            License.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(licenseId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + licenseId)

        # Return a license object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)
