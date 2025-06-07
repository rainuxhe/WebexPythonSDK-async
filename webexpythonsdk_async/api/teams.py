from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "teams"
OBJECT_TYPE = "team"


class TeamsAPI:
    """Webex Teams API.

    Wraps the Webex Teams API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new TeamsAPI object with the provided AsyncRestSession.

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
    async def list(self, max=100, **request_parameters):
        """List teams to which the authenticated user belongs.

        This method supports Webex's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all teams returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            max(int): Limit the maximum number of items returned from the Webex
                service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the teams returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(max, int, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            max=max,
        )

        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=params)

        # # Yield team objects created from the returned items JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

    async def create(self, name, **request_parameters):
        """Create a team.

        The authenticated user is automatically added as a member of the team.

        Args:
            name(str): A user-friendly name for the team.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Team: A Team object with the details of the created team.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(name, str)

        post_data = dict_from_items_with_values(
            request_parameters,
            name=name,
        )

        # API request
        json_data = await self._session.post(API_ENDPOINT, json=post_data)

        # Return a team object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, teamId):
        """Get the details of a team, by ID.

        Args:
            teamId(str): The ID of the team to be retrieved.

        Returns:
            Team: A Team object with the details of the requested team.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(teamId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + teamId)

        # Return a team object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def update(self, teamId, name, **request_parameters):
        """Update details for a team, by ID.

        Args:
            teamId(str): The team ID.
            name(str): A user-friendly name for the team.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Team: A Team object with the updated Webex team details.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(teamId, str)
        check_type(name, str)

        put_data = dict_from_items_with_values(
            request_parameters,
            name=name,
        )

        # API request
        json_data = await self._session.put(API_ENDPOINT + "/" + teamId, json=put_data)

        # Return a team object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def delete(self, teamId):
        """Delete a team.

        Args:
            teamId(str): The ID of the team to be deleted.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(teamId, str)

        # API request
        await self._session.delete(API_ENDPOINT + "/" + teamId)
