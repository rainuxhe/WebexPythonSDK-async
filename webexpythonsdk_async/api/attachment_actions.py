from ..restsession import AsyncRestSession
from ..utils import check_type, dict_from_items_with_values


API_ENDPOINT = "attachment/actions"
OBJECT_TYPE = "attachment_action"


class AttachmentActionsAPI:
    """Webex Attachment Actions API.

    Wraps the Webex Attachment Actions API and exposes the API as
    native Python methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new AttachmentActionsAPI object.

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
                API calls to the Webex service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, AsyncRestSession)
        
        self._session = session
        self._object_factory = object_factory

    async def create(self, type, messageId, inputs, **request_parameters):
        """Create a new attachment action.

        Args:
            type(str): The type of action to perform.
            messageId(str): The ID of the message which contains the
                attachment.
            inputs(dict): The attachment action's inputs.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            AttachmentAction: A attachment action object with the details of
            the created attachment action.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.
            ValueError: If the files parameter is a list of length > 1, or if
                the string in the list (the only element in the list) does not
                contain a valid URL or path to a local file.

        """
        check_type(type, str)
        check_type(messageId, str)
        check_type(inputs, dict)

        post_data = dict_from_items_with_values(request_parameters, type=type, messageId=messageId, inputs=inputs)

        json_data = await self._session.post(API_ENDPOINT, json=post_data)

        # Return a attachment action object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, id):
        """Get the details for a attachment action, by ID.

        Args:
            id(str): A unique identifier for the attachment action.

        Returns:
            AttachmentAction: A Attachment Action object with the details of
            the requested attachment action.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(id, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + id)

        # Return a message object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)
