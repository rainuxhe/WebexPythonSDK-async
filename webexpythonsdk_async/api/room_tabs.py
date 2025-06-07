from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "room/tabs"
OBJECT_TYPE = "room_tab"


class RoomTabsAPI:
    """Webex Room Tabs API.

    Wraps the Webex Room Tabs API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new RoomTabsAPI object with the provided AsyncRestSession.

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
    async def list(self, roomId, **request_parameters):
        """Lists all Room Tabs of a room.

        This method supports Webex's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all room tabs returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            roomId(str): List Room Tabs associated with a room, by ID.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the room tabs returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roomId, str)

        params = dict_from_items_with_values(
            request_parameters,
            roomId=roomId,
        )

        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=params)

        # # Yield room objects created from the returned items JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

    async def create(self, roomId, contentUrl, displayName, **request_parameters):
        """Create a room tab.

        Add a tab with a content url to a room that can be accessed in the room

        Args:
            roomId(str): A unique identifier for the room.
            contentUrl(str): Content Url of the Room Tab.
                Needs to use the https protocol.
            displayName(str): A user-friendly name for the room.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).
        Returns:
            RoomTab: A Room Tab with the details of the created room tab.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roomId, str)
        check_type(contentUrl, str)
        check_type(displayName, str)

        post_data = dict_from_items_with_values(
            request_parameters,
            roomId=roomId,
            contentUrl=contentUrl,
            displayName=displayName,
        )

        # API request
        json_data = await self._session.post(API_ENDPOINT, json=post_data)

        # Return a room object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, roomTabId):
        """Get the details of a room tab, by ID.

        Args:
            roomTabId(str): The ID of the room tab to be retrieved.

        Returns:
            Room: A RoomTab object with the details of the requested room tab.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roomTabId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + roomTabId)

        # Return a room object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def update(self, roomTabId, roomId, contentUrl, displayName, **request_parameters):
        """Updates the content url of a Room Tab by ID.

        Args:
            roomTabId(str): The unique identifier for the Room Tab.
            roomId(str): The room ID.
            contentUrl(str): Content Url of the Room Tab.
                Needs to use the https protocol.
            displayName(str): A user-friendly name for the room.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Room: A Room object with the updated Webex room details.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roomTabId, str)
        check_type(roomId, str)
        check_type(contentUrl, str)
        check_type(displayName, str)

        put_data = dict_from_items_with_values(
            request_parameters,
            roomTabId=roomTabId,
            roomId=roomId,
            contentUrl=contentUrl,
            displayName=displayName,
        )

        # API request
        json_data = await self._session.put(API_ENDPOINT + "/" + roomTabId, json=put_data)

        # Return a room object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def delete(self, roomTabId):
        """Delete a room tab.

        Args:
            roomTabId(str): The ID of the room tab to be deleted.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(roomTabId, str)

        # API request
        await self._session.delete(API_ENDPOINT + "/" + roomTabId)
