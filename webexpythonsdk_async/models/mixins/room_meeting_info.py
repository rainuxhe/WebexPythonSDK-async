class RoomMeetingInfoBasicPropertiesMixin(object):
    """Room basic properties."""

    @property
    def roomId(self):
        """A unique identifier for the room."""
        return self._json_data.get("roomId")

    @property
    def meetingLink(self):
        """The Webex meeting URL for the room."""
        return self._json_data.get("meetingLink")

    @property
    def sipAddress(self):
        """The SIP address for the room."""
        return self._json_data.get("sipAddress")

    @property
    def meetingNumber(self):
        """The Webex meeting number for the room."""
        return self._json_data.get("meetingNumber")

    @property
    def callInTollFreeNumber(self):
        """The toll-free PSTN number for the room."""
        return self._json_data.get("callInTollFreeNumber")

    @property
    def callInTollNumber(self):
        """The toll (local) PSTN number for the room."""
        return self._json_data.get("callInTollNumber")
