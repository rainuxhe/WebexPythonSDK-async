from webexpythonsdk_async.utils import WebexDateTime


class MessageBasicPropertiesMixin(object):
    """Message basic properties."""

    @property
    def id(self):
        """The unique identifier for the message."""
        return self._json_data.get("id")

    @property
    def parentId(self):
        """The unique identifier for the parent message."""
        return self._json_data.get("parentId")

    @property
    def roomId(self):
        """The room ID of the message."""
        return self._json_data.get("roomId")

    @property
    def roomType(self):
        """The type of room.

        Room Type Enum:
            `direct`: 1:1 room
            `group`: Group room
        """
        return self._json_data.get("roomType")

    @property
    def toPersonId(self):
        """The person ID of the recipient when sending a 1:1 message."""
        return self._json_data.get("toPersonId")

    @property
    def toPersonEmail(self):
        """The email address of the recipient when sending a 1:1 message."""
        return self._json_data.get("toPersonEmail")

    @property
    def text(self):
        """The message, in plain text."""
        return self._json_data.get("text")

    @property
    def markdown(self):
        """The message, in Markdown format."""
        return self._json_data.get("markdown")

    @property
    def html(self):
        """The text content of the message, in HTML format.

        This read-only property is used by the Webex clients.
        """
        return self._json_data.get("html")

    @property
    def files(self):
        """Public URLs for files attached to the message."""
        return self._json_data.get("files")

    @property
    def personId(self):
        """The person ID of the message author."""
        return self._json_data.get("personId")

    @property
    def personEmail(self):
        """The email address of the message author."""
        return self._json_data.get("personEmail")

    @property
    def mentionedPeople(self):
        """People IDs for anyone mentioned in the message."""
        return self._json_data.get("mentionedPeople")

    @property
    def mentionedGroups(self):
        """Group names for the groups mentioned in the message."""
        return self._json_data.get("mentionedGroups")

    @property
    def attachments(self):
        """Message content attachments attached to the message."""
        return self._json_data.get("attachments")

    @property
    def created(self):
        """The date and time the message was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None

    @property
    def updated(self):
        """The date and time the message was updated."""
        updated = self._json_data.get("updated")
        if updated:
            return WebexDateTime.strptime(updated)
        else:
            return None
