class MeetingTemplateBasicPropertiesMixin:
    """MeetingTemplate basic properties."""

    @property
    def id(self):
        """Unique id for meeting template"""
        return self._json_data.get("id")

    @property
    def name(self):
        """Name of the meeting template"""
        return self._json_data.get("name")

    @property
    def locale(self):
        """Locale for the meeting template"""
        return self._json_data.get("locale")

    @property
    def siteUrl(self):
        """Site URL for the meeting template"""
        return self._json_data.get("siteUrl")

    @property
    def templateType(self):
        """Type of the meeting template (meeting, webinar)"""
        return self._json_data.get("templateType")

    @property
    def isDefault(self):
        """Whether or not the meeting template is a default template"""
        return self._json_data.get("isDefault")

    @property
    def isStandard(self):
        """Whether or not the meeting template is a standard template"""
        return self._json_data.get("isStandard")

    @property
    def meeting(self):
        """Meeting object which is used as a template to create a meeting.

        Meeting object which is used to create a meeting by the meeting
        template. Please note that the meeting object should be used to create
        a meeting immediately.
        """
        return self._json_data.get("meeting")
