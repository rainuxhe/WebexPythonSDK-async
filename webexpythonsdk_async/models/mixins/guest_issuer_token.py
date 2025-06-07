class GuestIssuerTokenBasicPropertiesMixin:
    """Guest issuer token basic properties"""

    @property
    def token(self):
        return self._json_data.get("token")

    @property
    def expiresIn(self):
        return self._json_data.get("expiresIn")
