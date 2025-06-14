from webexpythonsdk_async.config import (
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
)
from webexpythonsdk_async.environment import WEBEX_ACCESS_TOKEN
from webexpythonsdk_async.exceptions import AccessTokenError
from webexpythonsdk_async.models.immutable import immutable_data_factory
from webexpythonsdk_async.restsession import AsyncRestSession
from webexpythonsdk_async.utils import check_type
from .access_tokens import AccessTokensAPI
from .admin_audit_events import AdminAuditEventsAPI
from .attachment_actions import AttachmentActionsAPI
from .events import EventsAPI
from .guest_issuer import GuestIssuerAPI
from .licenses import LicensesAPI
from .memberships import MembershipsAPI
from .messages import MessagesAPI
from .organizations import OrganizationsAPI
from .people import PeopleAPI
from .roles import RolesAPI
from .rooms import RoomsAPI
from .room_tabs import RoomTabsAPI
from .recordings import RecordingsAPI
from .team_memberships import TeamMembershipsAPI
from .teams import TeamsAPI
from .webhooks import WebhooksAPI
from .meetings import MeetingsAPI
from .meeting_templates import MeetingTemplatesAPI
from .meeting_invitees import MeetingInviteesAPI
from .meeting_registrants import MeetingRegistrantsAPI

import os


class AsyncWebexAPI(object):
    """Webex API wrapper.

    Creates a 'session' for all API calls through a created WebexAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    WebexAPI wraps all of the individual Webex APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
        wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
        object_factory=immutable_data_factory,
        client_id=None,
        client_secret=None,
        oauth_code=None,
        redirect_uri=None,
        proxies=None,
        be_geo_id=None,
        caller=None,
        disable_ssl_verify=False,
    ):
        """Create a new WebexAPI object.

        An access token must be used when interacting with the Webex API.
        This package supports three methods for you to provide that access
        token:

          1. You may manually specify the access token via the `access_token`
             argument, when creating a new WebexAPI object.

          2. If an access_token argument is not supplied, the package checks
             for a WEBEX_ACCESS_TOKEN environment variable.

          3. Provide the parameters (client_id, client_secret, oauth_code and
             oauth_redirect_uri) from your oauth flow.

        An AccessTokenError is raised if an access token is not provided
        via one of these two methods.

        Args:
            access_token(str): The access token to be used for API
                calls to the Webex service.  Defaults to checking for a
                WEBEX_ACCESS_TOKEN environment variable.
            base_url(str): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to webexpythonsdk_async.DEFAULT_BASE_URL.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to
                webexpythonsdk_async.config.DEFAULT_SINGLE_REQUEST_TIMEOUT.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to
                webexpythonsdk_async.config.DEFAULT_WAIT_ON_RATE_LIMIT.
            object_factory(callable): The factory function to use to create
                Python objects from the returned Webex JSON data objects.
            client_id(str): The client id of your integration. Provided
                upon creation in the portal.
            client_secret(str): The client secret of your integration.
                Provided upon creation in the portal.
            oauth_code(str): The oauth authorization code provided by
                the user oauth process.
            oauth_redirect_uri(str): The redirect URI used in the user
                OAuth process.
            proxies(dict): Dictionary of proxies passed on to the requests
                session.
            be_geo_id(str): Optional partner identifier for API usage
                tracking.  Defaults to checking for a BE_GEO_ID environment
                variable.
            caller(str): Optional  identifier for API usage tracking.
                Defaults to checking for a WEBEX_PYTHON_SDK_CALLER environment
                variable.
            disable_ssl_verify(bool): Optional boolean flag to disable ssl
                verification. Defaults to False. If set to True, the requests
                session won't verify ssl certs anymore.

        Returns:
            WebexAPI: A new WebexAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.

        """
        check_type(access_token, str, optional=True)
        check_type(base_url, str, optional=True)
        check_type(single_request_timeout, int, optional=True)
        check_type(wait_on_rate_limit, bool, optional=True)
        check_type(client_id, str, optional=True)
        check_type(client_secret, str, optional=True)
        check_type(oauth_code, str, optional=True)
        check_type(redirect_uri, str, optional=True)
        check_type(proxies, dict, optional=True)
        check_type(be_geo_id, str, optional=True)
        check_type(caller, str, optional=True)
        check_type(disable_ssl_verify, bool, optional=True)

        access_token = access_token or WEBEX_ACCESS_TOKEN

        # Init AccessTokensAPI wrapper early to use for oauth requests
        self.access_tokens = AccessTokensAPI(
            base_url,
            object_factory,
            single_request_timeout=single_request_timeout,
        )

        # Check if the user has provided the required oauth parameters
        oauth_param_list = [client_id, client_secret, oauth_code, redirect_uri]
        if not access_token and all(oauth_param_list):
            access_token = self.access_tokens.get(
                client_id=client_id,
                client_secret=client_secret,
                code=oauth_code,
                redirect_uri=redirect_uri,
            ).access_token

        # Set optional API metrics tracking variables from env vars if there
        be_geo_id = be_geo_id or os.environ.get("BE_GEO_ID")
        caller = caller or os.environ.get("WEBEX_PYTHON_SDK_CALLER")

        # If an access token hasn't been provided as a parameter, environment
        # variable, or obtained via an OAuth exchange raise an error.
        if not access_token:
            raise AccessTokenError(
                "You must provide a Webex access token to interact with "
                "the Webex APIs, either via a WEBEX_ACCESS_TOKEN "
                "environment variable or via the access_token argument."
            )

        # Create the API session
        # All of the API calls associated with a WebexAPI object will
        # leverage a single RESTful 'session' connecting to the Webex
        # cloud.
        self._session = AsyncRestSession(
            access_token=access_token,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
            proxies=proxies,
            be_geo_id=be_geo_id,
            caller=caller,
            disable_ssl_verify=disable_ssl_verify,
        )

        # API wrappers
        self.admin_audit_events = AdminAuditEventsAPI(
            self._session,
            object_factory,
        )
        self.attachment_actions = AttachmentActionsAPI(
            self._session,
            object_factory,
        )
        self.events = EventsAPI(self._session, object_factory)
        self.guest_issuer = GuestIssuerAPI(self._session, object_factory)
        self.licenses = LicensesAPI(self._session, object_factory)
        self.memberships = MembershipsAPI(self._session, object_factory)
        self.messages = MessagesAPI(self._session, object_factory)
        self.organizations = OrganizationsAPI(self._session, object_factory)
        self.people = PeopleAPI(self._session, object_factory)
        self.roles = RolesAPI(self._session, object_factory)
        self.rooms = RoomsAPI(self._session, object_factory)
        self.room_tabs = RoomTabsAPI(self._session, object_factory)
        self.teams = TeamsAPI(self._session, object_factory)
        self.team_memberships = TeamMembershipsAPI(
            self._session,
            object_factory,
        )
        self.webhooks = WebhooksAPI(self._session, object_factory)
        self.recordings = RecordingsAPI(self._session, object_factory)
        self.meetings = MeetingsAPI(self._session, object_factory)
        self.meeting_templates = MeetingTemplatesAPI(self._session, object_factory)
        self.meeting_invitees = MeetingInviteesAPI(self._session, object_factory)
        self.meeting_registrants = MeetingRegistrantsAPI(self._session, object_factory)

    @property
    def access_token(self):
        """The access token used for API calls to the Webex service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    # Create a class attribute for the Access Tokens API that can be accessed
    # before WebexAPI object is initialized.
    access_tokens = AccessTokensAPI(
        base_url=DEFAULT_BASE_URL,
        object_factory=immutable_data_factory,
        single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
    )

    @classmethod
    async def from_oauth_code(cls, client_id: str, client_secret: str, code: str, redirect_uri: str):
        """Create a new WebexAPI connection object using an OAuth code.

        Exchange an Authorization Code for an Access Token, then use the access
        token to create a new WebexAPI connection object.

        Args:
            client_id(str): Provided when you created your integration.
            client_secret(str): Provided when you created your
                integration.
            code(str): The Authorization Code provided by the user
                OAuth process.
            redirect_uri(str): The redirect URI used in the user OAuth
                process.

        Returns:
            WebexAPI: A new WebexAPI object initialized with the
            access token from the OAuth Authentication Code exchange.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.
        """
        token_obj = await cls.access_tokens.get(client_id, client_secret, code, redirect_uri)

        return cls(access_token=token_obj.access_token)

    @classmethod
    async def from_oauth_refresh(cls, client_id, client_secret, refresh_token):
        """Create a new WebexAPI connection object using an OAuth refresh.

        Exchange a refresh token for an Access Token, then use the access
        token to create a new WebexAPI connection object.

        Args:
            client_id(str): Provided when you created your integration.
            client_secret(str): Provided when you created your
                integration.
            refresh_token(str): Provided when you requested the Access
                Token.

        Returns:
            WebexAPI: A new WebexAPI object initialized with the
            access token from the OAuth Refresh Token exchange.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex cloud returns an error.
        """
        token_obj = await cls.access_tokens.refresh(client_id, client_secret, refresh_token)
        return cls(access_token=token_obj.access_token)
