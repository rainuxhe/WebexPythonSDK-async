class RoleBasicPropertiesMixin(object):
    """Role basic properties."""

    @property
    def id(self):
        """A unique identifier for the role."""
        return self._json_data.get("id")

    @property
    def name(self):
        """The name of the role."""
        return self._json_data.get("name")
