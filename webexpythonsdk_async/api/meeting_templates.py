from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "meetings/templates"
OBJECT_TYPE = "meetingTemplate"


class MeetingTemplatesAPI:
    """Webex MeetingTemplates API.

    Wraps the Webex MeetingTemplates API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Init a new MeetingTemplatesAPI object with the provided AsyncRestSession.

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
                API calls to the Webex service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, AsyncRestSession)

        super().__init__()

        self._session = session
        self._object_factory = object_factory

    # @generator_container
    async def list(
        self,
        templateType=None,
        locale=None,
        isDefault=None,
        isStandard=None,
        hostEmail=None,
        siteUrl=None,
        headers=None,
        **request_parameters,
    ):
        """List meetingTemplates.

        Use query parameters to filter the response.

        This method supports Webex's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all memberships returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            templateType (str): Meeting template types (meeting,
                webinar).
            locale (str): Locale for the meeting template (i.e. en_US).
            isDefault (bool): Flag to indicate if default or non-default
                meeting templates are returned.
            isStandard (bool): Flag to indicate if standard or non-standard
                meeting templates are returned.
            hostEmail (bool): Email address of a meeting host (Requires
                admin-level scope).
            siteUrl (bool): URL of the Webex site from which we are listing.
            headers(dict): Additional headers to be passed.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the meetingTemplates returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(templateType, str, optional=True)
        check_type(locale, str, optional=True)
        check_type(isDefault, bool, optional=True)
        check_type(isStandard, bool, optional=True)
        check_type(hostEmail, bool, optional=True)
        check_type(siteUrl, bool, optional=True)
        check_type(headers, dict, optional=True)

        headers = headers or {}

        params = dict_from_items_with_values(
            request_parameters,
            templateType=templateType,
            locale=locale,
            isDefault=isDefault,
            isStandard=isStandard,
            hostEmail=hostEmail,
            siteUrl=siteUrl,
        )

        # API request - get items

        # Update headers
        for k, v in headers.items():
            self._session.headers[k] = v
        # items = await self._session.get_items(API_ENDPOINT, params=params)
        async for item in self._session.get_items(API_ENDPOINT, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

        # Remove headers
        for k in headers.keys():
            del self._session.headers[k]

        # Yield membership objects created from the returned items JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)

    async def get(self, meetingTemplateId):
        """Get details for a meetingTemplate, by ID.

        Args:
            meetingTemplateId(str): The meetingTemplate ID.

        Returns:
            MeetingTemplate: A MeetingTemplate object with the details of the
            requested meetingTemplate.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(meetingTemplateId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + meetingTemplateId)

        # Return a membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)
