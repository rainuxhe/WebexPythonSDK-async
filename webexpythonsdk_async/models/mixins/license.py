class LicenseBasicPropertiesMixin:
    """License basic properties."""

    @property
    def id(self):
        """A unique identifier for the license."""
        return self._json_data.get("id")

    @property
    def name(self):
        """Name of the licensed feature."""
        return self._json_data.get("name")

    @property
    def totalUnits(self):
        """Total number of license units allocated."""
        return self._json_data.get("totalUnits")

    @property
    def consumedUnits(self):
        """Total number of license units consumed."""
        return self._json_data.get("consumedUnits")

    @property
    def subscriptionId(self):
        """The subscription ID associated with this license.

        This ID is used in other systems, such as Webex Control Hub.
        """
        return self._json_data.get("subscriptionId")

    @property
    def siteUrl(self):
        """The Webex Meetings site associated with this license."""
        return self._json_data.get("siteUrl")

    @property
    def siteType(self):
        """The type of site associated with this license.

        `Control Hub managed site` the site is managed by Webex Control Hub.

        `Linked site` the site is a linked site

        `Site Admin managed site` the site is managed by Site Administration
        """
        return self._json_data.get("siteType")
