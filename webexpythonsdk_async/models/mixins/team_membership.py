from webexpythonsdk_async.utils import WebexDateTime


class TeamMembershipBasicPropertiesMixin(object):
    """Team Membership basic properties."""

    @property
    def id(self):
        """A unique identifier for the team membership."""
        return self._json_data.get("id")

    @property
    def teamId(self):
        """The team ID."""
        return self._json_data.get("teamId")

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
        """Whether or not the participant is a team moderator."""
        return self._json_data.get("isModerator")

    @property
    def created(self):
        """The date and time when the team membership was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
