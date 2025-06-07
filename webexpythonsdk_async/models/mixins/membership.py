import warnings

from webexpythonsdk_async.utils import WebexDateTime


class MembershipBasicPropertiesMixin(object):
    """Membership basic properties."""

    @property
    def id(self):
        """A unique identifier for the membership."""
        return self._json_data.get("id")

    @property
    def roomId(self):
        """The room ID."""
        return self._json_data.get("roomId")

    @property
    def personId(self):
        """The person ID."""
        return self._json_data.get("personId")

    @property
    def personEmail(self):
        """The email address of the person."""
        return self._json_data.get("personEmail")

    @property
    def personDisplayName(self):
        """The display name of the person."""
        return self._json_data.get("personDisplayName")

    @property
    def personOrgId(self):
        """The organization ID of the person."""
        return self._json_data.get("personOrgId")

    @property
    def isModerator(self):
        """Whether or not the participant is a room moderator."""
        return self._json_data.get("isModerator")

    @property
    def isMonitor(self):
        """Whether or not the participant is a monitoring bot (deprecated)."""
        warnings.warn(
            "The `isMonitor` attribute has been deprecated.",
            DeprecationWarning,
            stacklevel=1,
        )
        return self._json_data.get("isMonitor")

    @property
    def created(self):
        """The date and time when the membership was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
