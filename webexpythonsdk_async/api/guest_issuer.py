from ..restsession import AsyncRestSession
from ..utils import (
    check_type,
)


import jwt
import base64

API_ENDPOINT = "jwt"
OBJECT_TYPE = "guest_issuer_token"


class GuestIssuerAPI:
    """Webex Guest Issuer API.

    Wraps the Webex Guest Issuer API and exposes the API as native
    methods that return native Python objects.

    """

    def __init__(self, session: AsyncRestSession, object_factory):
        """Initialize a new GuestIssuerAPI object with the provided AsyncRestSession

        Args:
            session(AsyncRestSession): The RESTful session object to be used for
            API calls to the Webex service

        Raises:
            TypeError: If the parameter types are incorrect
        """
        check_type(session, AsyncRestSession)

        self._session = session
        self._object_factory = object_factory

    async def create(self, sub, name, iss, exp, secret):
        """Create a new guest issuer using the provided issuer token.

        This function returns a guest issuer with an api access token.

        Args:
            sub(str): The subject of the token. This is your unique
                and public identifier for the guest user. This claim may
                contain only letters, numbers, and hyphens.
            name(str): The display name of the guest user. This will be
                the name shown in Webex clients.
            iss(str): The issuer of the token. Use the Guest
                Issuer ID provided in My Webex Apps.
            exp(str): The exp time of the token, as a UNIX
                timestamp in seconds. Use the lowest practical value for the
                use of the token. This is not the exp time for the guest
                user's session.
            secret(str): Use the secret Webex provided you when you
                created your Guest Issuer App. The secret will be used to sign
                the token request.

        Returns:
            GuestIssuerToken: A Guest Issuer token with a valid access token.

        Raises:
            TypeError: If the parameter types are incorrect
            ApiError: If the webex teams cloud returns an error.
        """
        check_type(sub, str)
        check_type(name, str)
        check_type(iss, str)
        check_type(exp, str)
        check_type(secret, str)

        payload = {"sub": sub, "name": name, "iss": iss, "exp": exp}

        key = base64.b64decode(secret)
        jwt_token = jwt.encode(payload, key, algorithm="HS256")

        headers = {"Authorization": "Bearer " + jwt_token}

        json_data = await self._session.post(API_ENDPOINT + "/" + "login", headers=headers)

        return self._object_factory(OBJECT_TYPE, json_data)
