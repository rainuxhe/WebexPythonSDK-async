from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
)


API_ENDPOINT = "roles"
OBJECT_TYPE = "role"


class RolesAPI:
    """Webex Roles API.

    Wraps the Webex Roles API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new RolesAPI object with the provided AsyncRestSession.

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
                API calls to the Webex service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, AsyncRestSession)

        self._session = session
        self._object_factory = object_factory

    # @generator_container
    async def list(self, **request_parameters):
        """List all roles.

        Args:
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the roles returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=request_parameters)

        # # Yield role objects created from the returned JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=request_parameters):
            yield self._object_factory(OBJECT_TYPE, item)

    async def get(self, roleId):
        """Get the details of a Role, by ID.

        Args:
            roleId(str): The ID of the Role to be retrieved.

        Returns:
            Role: A Role object with the details of the requested Role.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roleId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + roleId)

        # Return a role object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)
