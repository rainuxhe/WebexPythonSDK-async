class MeetingInviteeBasicPropertiesMixin:
    """MeetingInvitee basic properties."""

    @property
    def id(self):
        """Unique id for the meeting invitee"""
        return self._json_data.get("id")

    @property
    def email(self):
        """Email address for the meeting invitee"""
        return self._json_data.get("email")

    @property
    def displayName(self):
        """Display name of the meeting invitee"""
        return self._json_data.get("displayName")

    @property
    def coHost(self):
        """CoHost status of the invitee"""
        return self._json_data.get("coHost")

    @property
    def meetingId(self):
        """Unique id for the meeting that the invitee is part of"""
        return self._json_data.get("meetingId")

    @property
    def panelist(self):
        """Flag to indicate if the invitee is panelist or not"""
        return self._json_data.get("panelist")
