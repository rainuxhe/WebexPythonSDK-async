from webexpythonsdk_async.utils import WebexDateTime


class RecordingBasicPropertiesMixin(object):
    """Recording basic properties"""

    @property
    def id(self):
        """The unique identifier for the recording."""
        return self._json_data.get("id")

    @property
    def meetingId(self):
        """Meeting identifier for the meeting instance.

        Unique identifier for the parent ended meeting instance that the
        recording belongs to.
        """
        return self._json_data.get("meetingId")

    @property
    def scheduledMeetingId(self):
        """Meeting identifier for the scheduled meeting.

        Unique identifier for the parent scheduled meeting which the recording
        belongs to.
        """
        return self._json_data.get("scheduledMeetingId")

    @property
    def topic(self):
        """The recording topic."""
        return self._json_data.get("topic")

    @property
    def meetingSeriesId(self):
        """Meeting series identifier.

        Unique identifier for the parent meeting series which the recording
        belongs to.
        """
        return self._json_data.get("meetingSeriesId")

    @property
    def createTime(self):
        """Recording creation time.

        The date and time recording was created in ISO 8601 compliant format.
        """
        created = self._json_data.get("createTime")
        if created:
            return WebexDateTime.strptime(created)

    @property
    def timeRecorded(self):
        """The date and time recording started in ISO 8601 compliant format."""
        recorded = self._json_data.get("timeRecorded")
        if recorded:
            return WebexDateTime.strptime(recorded)

    @property
    def siteUrl(self):
        """Site URL for the recording."""
        return self._json_data.get("siteUrl")

    @property
    def downloadUrl(self):
        """The download link for recording."""
        return self._json_data.get("downloadUrl")

    @property
    def playbackUrl(self):
        """The playback link for recording."""
        return self._json_data.get("playbackUrl")

    @property
    def password(self):
        """The recording's password."""
        return self._json_data.get("password")

    @property
    def format(self):
        """The recording's file format."""
        return self._json_data.get("format")

    @property
    def serviceType(self):
        """The recording's service type."""
        return self._json_data.get("serviceType")

    @property
    def durationSeconds(self):
        """The duration of the recording, in seconds."""
        return self._json_data.get("durationSeconds")

    @property
    def sizeBytes(self):
        """The size of the recording file, in bytes."""
        return self._json_data.get("sizeBytes")

    @property
    def shareToMe(self):
        """Whether or not the recording has been shared to the current user."""
        return self._json_data.get("shareToMe")

    @property
    def integrationTags(self):
        """Integration tags.

        External keys of the parent meeting created by an integration
        application.
        """
        return self._json_data.get("integrationTags")
