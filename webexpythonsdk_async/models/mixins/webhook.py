from webexpythonsdk_async.utils import WebexDateTime


class WebhookBasicPropertiesMixin(object):
    """Webhook basic properties."""

    @property
    def id(self):
        """A unique identifier for the webhook."""
        return self._json_data.get("id")

    @property
    def name(self):
        """A user-friendly name for the webhook."""
        return self._json_data.get("name")

    @property
    def targetUrl(self):
        """The URL that receives POST requests for each event."""
        return self._json_data.get("targetUrl")

    @property
    def resource(self):
        """The resource type for the webhook.

        Creating a webhook requires 'read' scope on the resource the webhook
        is for.

        Webhook Resource Enum:
            `all`: Subscribe to all resources
            `memberships`: The Memberships resource
            `messages`: The Messages resource
            `rooms`: The Rooms resource
        """
        return self._json_data.get("resource")

    @property
    def event(self):
        """The event type for the webhook.

        Webhook Event Type Enum:
            `all`: Subscribe to all events
            `created`: An object was created
            `updated`: An object was updated
            `deleted`: An object was deleted
        """
        return self._json_data.get("event")

    @property
    def filter(self):
        """The filter that defines the webhook scope."""
        return self._json_data.get("filter")

    @property
    def secret(self):
        """The secret used to generate payload signature."""
        return self._json_data.get("secret")

    @property
    def orgId(self):
        """The ID of the organization that owns the webhook."""
        return self._json_data.get("orgId")

    @property
    def createdBy(self):
        """The ID of the person that created the webhook."""
        return self._json_data.get("createdBy")

    @property
    def appId(self):
        """The ID of the application that created the webhook."""
        return self._json_data.get("appId")

    @property
    def ownedBy(self):
        """Indicates if the webhook is owned by the `org` or the `creator`.

        Webhooks owned by the creator can only receive events that are
        accessible to the creator of the webhook. Those owned by the
        organization will receive events that are visible to anyone in the
        organization.

        Webhook Owned By Enum:
            `org`
            `creator`
        """
        return self._json_data.get("ownedBy")

    @property
    def status(self):
        """The status of the webhook.

        Webhook Status Enum:
            `active`: The webhook is active
            `inactive`: The webhook is inactive
        """
        return self._json_data.get("status")

    @property
    def created(self):
        """The date and time the webhook was created."""
        created = self._json_data.get("created")
        if created:
            return WebexDateTime.strptime(created)
        else:
            return None
