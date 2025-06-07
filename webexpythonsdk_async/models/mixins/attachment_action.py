from webexpythonsdk_async.utils import WebexDateTime


class AttachmentActionBasicPropertiesMixin:
    """Attachment Action basic properties."""

    @property
    def id(self):
        """A unique identifier for the action."""
        return self._json_data.get("id")

    @property
    def personId(self):
        """The ID of the person who performed the action."""
        return self._json_data.get("personId")

    @property
    def roomId(self):
        """The ID of the room the action was performed within."""
        return self._json_data.get("roomId")

    @property
    def type(self):
        """The type of action performed.

        Attachment action enum:
            'submit': submit filled in inputs
        """
        return self._json_data.get("type")

    @property
    def messageId(self):
        """The parent message the attachment action was performed on."""
        return self._json_data.get("messageId")

    @property
    def inputs(self):
        """The attachment action's inputs"""
        return self._json_data.get("inputs")

    @property
    def created(self):
        """The date and time the action was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
