from ..generator_containers import generator_container
from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = "people"
OBJECT_TYPE = "person"


class PeopleAPI:
    """Webex People API.

    Wraps the Webex People API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Initialize a new PeopleAPI object with the provided AsyncRestSession.

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
        email=None,
        displayName=None,
        id=None,
        orgId=None,
        max=None,
        **request_parameters,
    ):
        """List people in your organization.

        For most users, either the `email` or `displayName` parameter is
        required. Admin users can omit these fields and list all users in their
        organization.

        Response properties associated with a user's presence status, such as
        `status` or `lastActivity`, will only be displayed for people within
        your organization or an organization you manage. Presence information
        will not be shown if the authenticated user has disabled status
        sharing.

        This method supports Webex's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all people returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            email(str): The e-mail address of the person to be found.
            displayName(str): The complete or beginning portion of
                the displayName to be searched.
            id(str): List people by ID. Accepts up to 85 person IDs
                separated by commas.
            orgId(str): The organization ID.
            max(int): Limit the maximum number of items returned from the Webex
                service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the people returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(id, str, optional=True)
        check_type(email, str, optional=True)
        check_type(displayName, str, optional=True)
        check_type(orgId, str, optional=True)
        check_type(max, int, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            id=id,
            email=email,
            displayName=displayName,
            orgId=orgId,
            max=max,
        )

        # API request - get items
        # items = await self._session.get_items(API_ENDPOINT, params=params)

        # # Yield person objects created from the returned items JSON objects
        # for item in items:
        #     yield self._object_factory(OBJECT_TYPE, item)
        async for item in self._session.get_items(API_ENDPOINT, params=params):
            yield self._object_factory(OBJECT_TYPE, item)

    async def create(
        self,
        emails,
        phoneNumbers=None,
        extension=None,
        locationId=None,
        displayName=None,
        firstName=None,
        lastName=None,
        avatar=None,
        orgId=None,
        roles=None,
        licenses=None,
        department=None,
        manager=None,
        managerId=None,
        title=None,
        addresses=None,
        siteUrls=None,
        callingData=None,
        minResponse=None,
        **request_parameters,
    ):
        """Create a new user account for a given organization

        Only an admin can create a new user account.

        Args:
            emails(`list`): Email address(es) of the person (list of strings).
            phoneNumbers(`list`): Phone numbers for the person.
            extension(str): Webex Calling extension of the person.
            locationId(str): The ID of the location for this person.
            displayName(str): Full name of the person.
            firstName(str): First name of the person.
            lastName(str): Last name of the person.
            avatar(str): URL to the person's avatar in PNG format.
            orgId(str): ID of the organization to which this
                person belongs.
            roles(`list`): Roles of the person (list of strings containing
                the role IDs to be assigned to the person).
            licenses(`list`): Licenses allocated to the person (list of
                strings - containing the license IDs to be allocated to the
                person).
            department(str): The business department the user belongs
                to.
            manager(str): A manager identifier.
            managerId(str): Person ID of the manager.
            title(str): The person's title.
            addresses(`list`): A person's addresses.
            siteUrls(`list`): One or several site names where this user has an
                attendee role.
            callingData(bool): Include Webex Calling user details in the
                response.
            minResponse(bool): Set to true to improve performance by omitting
                person details and returning only the ID in the response when
                successful.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the details of the created person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(emails, list)
        check_type(phoneNumbers, list, optional=True)
        check_type(extension, str, optional=True)
        check_type(locationId, str, optional=True)
        check_type(displayName, str, optional=True)
        check_type(firstName, str, optional=True)
        check_type(lastName, str, optional=True)
        check_type(avatar, str, optional=True)
        check_type(orgId, str, optional=True)
        check_type(roles, list, optional=True)
        check_type(licenses, list, optional=True)
        check_type(department, str, optional=True)
        check_type(manager, str, optional=True)
        check_type(managerId, str, optional=True)
        check_type(title, str, optional=True)
        check_type(addresses, list, optional=True)
        check_type(siteUrls, list, optional=True)
        check_type(callingData, bool, optional=True)
        check_type(minResponse, bool, optional=True)

        post_data = dict_from_items_with_values(
            request_parameters,
            emails=emails,
            phoneNumbers=phoneNumbers,
            extension=extension,
            locationId=locationId,
            displayName=displayName,
            firstName=firstName,
            lastName=lastName,
            avatar=avatar,
            orgId=orgId,
            roles=roles,
            licenses=licenses,
            department=department,
            manager=manager,
            managerId=managerId,
            title=title,
            addresses=addresses,
            siteUrls=siteUrls,
        )

        params = dict_from_items_with_values(
            callingData=callingData,
            minResponse=minResponse,
        )

        # API request
        json_data = await self._session.post(API_ENDPOINT, params=params, json=post_data)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)

    async def get(self, personId):
        """Get a person's details, by ID.

        Args:
            personId(str): The ID of the person to be retrieved.

        Returns:
            Person: A Person object with the details of the requested person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(personId, str)

        # API request
        json_data = await self._session.get(API_ENDPOINT + "/" + personId)

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    async def update(
        self,
        personId,
        emails=None,
        displayName=None,
        firstName=None,
        lastName=None,
        avatar=None,
        orgId=None,
        roles=None,
        licenses=None,
        **request_parameters,
    ):
        """Update details for a person, by ID.

        Only an admin can update a person's details.

        Email addresses for a person cannot be changed via the Webex API.

        Include all details for the person. This action expects all user
        details to be present in the request. A common approach is to first GET
        the person's details, make changes, then PUT both the changed and
        unchanged values.

        Args:
            personId(str): The person ID.
            emails(`list`): Email address(es) of the person (list of strings).
            displayName(str): Full name of the person.
            firstName(str): First name of the person.
            lastName(str): Last name of the person.
            avatar(str): URL to the person's avatar in PNG format.
            orgId(str): ID of the organization to which this
                person belongs.
            roles(`list`): Roles of the person (list of strings containing
                the role IDs to be assigned to the person).
            licenses(`list`): Licenses allocated to the person (list of
                strings - containing the license IDs to be allocated to the
                person).
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the updated details.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(emails, list, optional=True)
        check_type(displayName, str, optional=True)
        check_type(firstName, str, optional=True)
        check_type(lastName, str, optional=True)
        check_type(avatar, str, optional=True)
        check_type(orgId, str, optional=True)
        check_type(roles, list, optional=True)
        check_type(licenses, list, optional=True)

        put_data = dict_from_items_with_values(
            request_parameters,
            emails=emails,
            displayName=displayName,
            firstName=firstName,
            lastName=lastName,
            avatar=avatar,
            orgId=orgId,
            roles=roles,
            licenses=licenses,
        )

        # API request
        json_data = await self._session.put(API_ENDPOINT + "/" + personId, json=put_data)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)

    async def delete(self, personId):
        """Remove a person from the system.

        Only an admin can remove a person.

        Args:
            personId(str): The ID of the person to be deleted.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.

        """
        check_type(personId, str)

        # API request
        await self._session.delete(API_ENDPOINT + "/" + personId)

    async def me(self):
        """Get the details of the person accessing the API.

        Raises:
            ApiError: If the Webex cloud returns an error.

        """
        # API request
        json_data = await self._session.get(API_ENDPOINT + "/me")

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)
