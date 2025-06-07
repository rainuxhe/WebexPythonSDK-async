from webexpythonsdk_async.utils import WebexDateTime


class OrganizationBasicPropertiesMixin(object):
    """Organization basic properties."""

    @property
    def id(self):
        """A unique identifier for the organization."""
        return self._json_data.get("id")

    @property
    def displayName(self):
        """Full name of the organization."""
        return self._json_data.get("displayName")

    @property
    def created(self):
        """The date and time the organization was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
