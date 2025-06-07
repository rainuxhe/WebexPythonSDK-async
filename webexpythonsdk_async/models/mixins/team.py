from webexpythonsdk_async.utils import WebexDateTime


class TeamBasicPropertiesMixin(object):
    """Team basic properties."""

    @property
    def id(self):
        """A unique identifier for the team."""
        return self._json_data.get("id")

    @property
    def name(self):
        """A user-friendly name for the team."""
        return self._json_data.get("name")

    @property
    def creatorId(self):
        """The ID of the person who created the team."""
        return self._json_data.get("creatorId")

    @property
    def created(self):
        """The date and time the team was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
