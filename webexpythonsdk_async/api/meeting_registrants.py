from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "meetings/{meetingId}/registrants"
OBJECT_TYPE = "meetingRegistrant"


class MeetingRegistrantsAPI:
    """Webex MeetingRegistrants API.

    Wraps the Webex MeetingRegistrants API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Init a new MeetingRegistrantsAPI object with the AsyncRestSession.

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
    async def list(
        self,
        meetingId,
        max=None,
        hostEmail=None,
        current=None,
        email=None,
        registrationTimeFrom=None,
        registrationTimeTo=None,
        headers=None,
        **request_parameters,
    ):
        """List meetingRegistrants.

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
            meetingId (str): Unique identifier for the meeting.
            max (int): Limit the maximum number of registrants in the response,
                up to 100.
            hostEmail (str): Email address for the meeting host.
            current (bool): Whether or not to retrieve only the current
                scheduled meeting of the meeting series, i.e. the meeting ready
                to join or start or the upcoming meeting of the meeting series.
            email (str): Registrant's email to filter registrants.
            registrationTimeFrom (str): The time registrants register a
                meeting starts from the specified date and time (inclusive) in
                any ISO 8601 compliant format.
            registrationTimeTo (str): The time registrants register a
                meeting before the specified date and time (exclusive) in any
                ISO 8601 compliant format.
            headers(dict): Additional headers to be passed.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the meetingRegistrants returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(meetingId, str)
        check_type(max, int, optional=True)
        check_type(hostEmail, str, optional=True)
        check_type(current, bool, optional=True)
        check_type(email, str, optional=True)
        check_type(registrationTimeFrom, str, optional=True)
        check_type(registrationTimeTo, str, optional=True)
        check_type(headers, dict, optional=True)

        headers = headers or {}

        params = dict_from_items_with_values(
            request_parameters,
            max=max,
            hostEmail=hostEmail,
            current=current,
            email=email,
            registrationTimeFrom=registrationTimeFrom,
            registrationTimeTo=registrationTimeTo,
        )

        # Add URL parameters to the API endpoint
        request_url = API_ENDPOINT.format(meetingId=meetingId)

        # API request - get items

        # Update headers
        for k, v in headers.items():
            self._session.headers[k] = v
        # items = await self._session.get_items(request_url, params=params)
        async for item in self._session.get_items(request_url, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

        # Remove headers
        for k in headers.keys():
            del self._session.headers[k]

        # Yield membership objects created from the returned items JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)

    async def create(
        self,
        meetingId,
        firstName,
        lastName,
        email,
        sendEmail=None,
        jobTitle=None,
        address1=None,
        address2=None,
        city=None,
        state=None,
        zipCode=None,
        countryRegion=None,
        workPhone=None,
        fax=None,
        customizedQuestions=None,
        **request_parameters,
    ):
        """Create a meetingRegistrant.

        Args:
            meetingId (str): Unique identifier for the meeting.
            firstName (str): Registrant's first name.
            lastName (str): Registrant's last name.
            email (str): Registrant's email.
            sendEmail (bool): If true send email to the registrant.
            jobTitle (str): Registrant's job title.
            address1 (str): Registrant's first address line.
            address2 (str): Registrant's second address line.
            city (str): Registrant's city name.
            state (str): Registrant's state.
            zipCode (int): Registrant's postal code.
            countryRegion (str): Registrant's country or region.
            workPhone (str): Registrant's work phone number.
            fax (str): Registrant's FAX number.
            customizedQuestions (list): List of registrant's answers for
                customized questions,
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MeetingRegistrant: A MeetingRegistrant object with the details of
                the created meetingRegistrant.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(meetingId, str)
        check_type(firstName, str)
        check_type(lastName, str)
        check_type(email, str)
        check_type(sendEmail, bool, optional=True)
        check_type(jobTitle, str, optional=True)
        check_type(address1, str, optional=True)
        check_type(address2, str, optional=True)
        check_type(city, str, optional=True)
        check_type(state, str, optional=True)
        check_type(zipCode, int, optional=True)
        check_type(countryRegion, str, optional=True)
        check_type(workPhone, str, optional=True)
        check_type(fax, str, optional=True)
        check_type(customizedQuestions, list, optional=True)

        post_data = dict_from_items_with_values(
            request_parameters,
            firstName=firstName,
            lastName=lastName,
            email=email,
            sendEmail=sendEmail,
            jobTitle=jobTitle,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zipCode=zipCode,
            countryRegion=countryRegion,
            workPhone=workPhone,
            fax=fax,
            customizedQuestions=customizedQuestions,
        )

        # Add URL parameters to the API endpoint
        request_url = API_ENDPOINT.format(meetingId=meetingId)

        # API request
        json_data = await self._session.post(request_url, json=post_data)

        # Return a membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, meetingId, meetingRegistrantId):
        """Get details for a meetingRegistrant, by ID.

        Args:
            meetingId (str): Unique identifier for the meeting.
            meetingRegistrantId(str): The meetingRegistrant ID.

        Returns:
            MeetingRegistrant: A MeetingRegistrant object with the details of
                the requested meetingRegistrant.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(meetingId, str)
        check_type(meetingRegistrantId, str)

        # Add URL parameters to the API endpoint
        request_url = API_ENDPOINT.format(meetingId=meetingId)

        # API request
        json_data = await self._session.get(request_url + "/" + meetingRegistrantId)

        # Return a membership object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def delete(self, meetingId, meetingRegistrantId):
        """Delete a meetingRegistrant, by ID.

        Args:
            meetingId (str): Unique identifier for the meeting.
            meetingRegistrantId(str): The meetingRegistrant ID.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(meetingId, str)
        check_type(meetingRegistrantId, str)

        # Add URL parameters to the API endpoint
        request_url = API_ENDPOINT.format(meetingId=meetingId)

        # API request
        await self._session.delete(request_url + "/" + meetingRegistrantId)
