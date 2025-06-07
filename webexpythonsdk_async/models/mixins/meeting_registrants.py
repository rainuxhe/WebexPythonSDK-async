class MeetingRegistrantBasicPropertiesMixin:
    """MeetingRegistrant basic properties."""

    @property
    def registrantId(self):
        """New registrant's ID."""
        return self._json_data.get("registrantId")

    @property
    def status(self):
        """New registrant's status."""
        return self._json_data.get("status")

    @property
    def firstName(self):
        """Registrant's first name."""
        return self._json_data.get("firstName")

    @property
    def lastName(self):
        """Registrant's last name."""
        return self._json_data.get("lastName")

    @property
    def email(self):
        """Registrant's email."""
        return self._json_data.get("email")

    @property
    def jobTitle(self):
        """Registrant's job title."""
        return self._json_data.get("jobTitle")

    @property
    def companyName(self):
        """Registrant's company."""
        return self._json_data.get("companyName")

    @property
    def address1(self):
        """Registrant's first address line."""
        return self._json_data.get("address1")

    @property
    def address2(self):
        """Registrant's second address line."""
        return self._json_data.get("address2")

    @property
    def city(self):
        """Registrant's city name."""
        return self._json_data.get("city")

    @property
    def state(self):
        """Registrant's state."""
        return self._json_data.get("state")

    @property
    def zipCode(self):
        """Registrant's postal code."""
        return self._json_data.get("zipCode")

    @property
    def countryRegion(self):
        """Registrant's country or region."""
        return self._json_data.get("countryRegion")

    @property
    def workPhone(self):
        """Registrant's work phone number."""
        return self._json_data.get("workPhone")

    @property
    def fax(self):
        """Registrant's FAX number."""
        return self._json_data.get("fax")

    @property
    def registrationTime(self):
        """Registrant's registration time."""
        return self._json_data.get("registrationTime")

    @property
    def customizedQuestions(self):
        """List of registrant's answers for customized questions,"""
        return self._json_data.get("customizedQuestions")

    @property
    def sourceId(self):
        """Registrant's source id."""
        return self._json_data.get("sourceId")

    @property
    def registrationId(self):
        """Registrant's registration ID."""
        return self._json_data.get("registrationId")
