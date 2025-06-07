from webexpythonsdk_async.utils import WebexDateTime


class RoomTabBasicPropertiesMixin(object):
    """Room Tab basic properties."""

    @property
    def id(self):
        """A unique identifier for the Room Tab."""
        return self._json_data.get("id")

    @property
    def displayName(self):
        """User-friendly name for the room tab."""
        return self._json_data.get("displayName")

    @property
    def contentUrl(self):
        """Content Url of the Room Tab."""
        return self._json_data.get("contentUrl")

    @property
    def creatorId(self):
        """The person ID of the person who created this Room Tab."""
        return self._json_data.get("creatorId")

    @property
    def created(self):
        """The date and time when the Room Tab was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
