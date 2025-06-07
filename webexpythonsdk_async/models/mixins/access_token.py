class AccessTokenBasicPropertiesMixin:
    """Access Token basic properties."""

    @property
    def access_token(self):
        """Webex access token."""
        return self._json_data.get("access_token")

    @property
    def expires_in(self):
        """Access token expiry time (in seconds)."""
        return self._json_data.get("expires_in")

    @property
    def refresh_token(self):
        """Refresh token used to request a new/refreshed access token."""
        return self._json_data.get("refresh_token")

    @property
    def refresh_token_expires_in(self):
        """Refresh token expiry time (in seconds)."""
        return self._json_data.get("refresh_token_expires_in")
