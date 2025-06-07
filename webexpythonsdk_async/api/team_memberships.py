from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "team/memberships"
OBJECT_TYPE = "team_membership"


class TeamMembershipsAPI:
    """Webex Team-Memberships API.

    Wraps the Webex Memberships API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Init a new TeamMembershipsAPI object with the provided AsyncRestSession.

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
    async def list(self, teamId, max=100, **request_parameters):
        """List team memberships for a team, by ID.

        This method supports Webex's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all team memberships returned by
        the query.  The generator will automatically request additional 'pages'
        of responses from Webex as needed until all responses have been
        returned. The container makes the generator safe for reuse.  A new API
        call will be made, using the same parameters that were specified when
        the generator was created, every time a new iterator is requested from
        the container.

        Args:
            teamId(str): List team memberships for a team, by ID.
            max(int): Limit the maximum number of items returned from the Webex
                service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the team memberships returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(teamId, str)
        check_type(max, int, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            teamId=teamId,
            max=max,
        )

        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=params)

        # # Yield team membership objects created from the returned items JSON
        # # objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

    async def create(
        self,
        teamId,
        personId=None,
        personEmail=None,
        isModerator=False,
        **request_parameters,
    ):
        """Add someone to a team by Person ID or email address.

        Add someone to a team by Person ID or email address; optionally making
        them a moderator.

        Args:
            teamId(str): The team ID.
            personId(str): The person ID.
            personEmail(str): The email address of the person.
            isModerator(bool): Set to True to make the person a team moderator.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            TeamMembership: A TeamMembership object with the details of the
            created team membership.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(teamId, str)
        check_type(personId, str, optional=True)
        check_type(personEmail, str, optional=True)
        check_type(isModerator, bool, optional=True)

        post_data = dict_from_items_with_values(
            request_parameters,
            teamId=teamId,
            personId=personId,
            personEmail=personEmail,
            isModerator=isModerator,
        )

        # API request
        json_data = await self._session.post(API_ENDPOINT, json=post_data)

        # Return a team membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, membershipId):
        """Get details for a team membership, by ID.

        Args:
            membershipId(str): The team membership ID.

        Returns:
            TeamMembership: A TeamMembership object with the details of the
            requested team membership.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(membershipId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + membershipId)

        # Return a team membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def update(self, membershipId, isModerator=None, **request_parameters):
        """Update a team membership, by ID.

        Args:
            membershipId(str): The team membership ID.
            isModerator(bool): Set to True to make the person a team moderator.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            TeamMembership: A TeamMembership object with the updated Webex
            team-membership details.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(membershipId, str)
        check_type(isModerator, bool, optional=True)

        put_data = dict_from_items_with_values(
            request_parameters,
            isModerator=isModerator,
        )

        # API request
        json_data = await self._session.put(API_ENDPOINT + "/" + membershipId, json=put_data)

        # Return a team membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def delete(self, membershipId):
        """Delete a team membership, by ID.

        Args:
            membershipId(str): The team membership ID.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(membershipId, str)

        # API request
        await self._session.delete(API_ENDPOINT + "/" + membershipId)
