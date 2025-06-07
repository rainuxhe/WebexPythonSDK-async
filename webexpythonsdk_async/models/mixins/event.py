from webexpythonsdk_async.utils import WebexDateTime


class EventBasicPropertiesMixin:
    """Event basic properties."""

    @property
    def id(self):
        """The unique identifier for the event."""
        return self._json_data.get("id")

    @property
    def resource(self):
        """The type of resource in the event.

        Event Resource Enum:
            `messages`
            `memberships`
        """
        return self._json_data.get("resource")

    @property
    def type(self):
        """The action which took place in the event.

        Event Type Enum:
            `created`
            `updated`
            `deleted`
        """
        return self._json_data.get("type")

    @property
    def appId(self):
        """The ID of the application for the event."""
        return self._json_data.get("appId")

    @property
    def actorId(self):
        """The ID of the person who performed the action."""
        return self._json_data.get("actorId")

    @property
    def orgId(self):
        """The ID of the organization for the event."""
        return self._json_data.get("orgId")

    @property
    def created(self):
        """The date and time of the event."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
