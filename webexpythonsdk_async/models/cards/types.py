from webexpythonsdk_async.models.cards.adaptive_card_component import (
    AdaptiveCardComponent,
)
import webexpythonsdk_async.models.cards.options as OPTIONS
from webexpythonsdk_async.models.cards.utils import (
    validate_input,
    validate_uri,
)


class BackgroundImage(AdaptiveCardComponent):
    """
    **Adaptive Card - Background Image Element**

    Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.
    """

    def __init__(
        self,
        url: object,
        fillMode: OPTIONS.ImageFillMode = None,
        horizontalAlignment: OPTIONS.HorizontalAlignment = None,
        verticalAlignment: OPTIONS.VerticalContentAlignment = None,
    ):
        """
        Initialize a new BackgroundImage element.

        Args:
            url (uri, Mandatory): The URL (or data url) of the image.
                Acceptable formats are PNG, JPEG, and GIF. Allowed value(s):
                uri
            fillMode (ImageFillMode, Optional): Describes how the image should
                fill the area. **_Defaults to None._** Allowed value(s):
                ImageFillMode.COVER, ImageFillMode.REPEAT_HORIZONTALLY,
                ImageFillMode.REPEAT_VERTICALLY, or ImageFillMode.REPEAT
            horizontalAlignment (HorizontalAlignment, Optional): Describes how
                the image should be aligned if it must be cropped or if using
                repeat fill mode. **_Defaults to None._** Allowed value(s):
                HorizontalAlignment.LEFT, HorizontalAlignment.CENTER, or
                HorizontalAlignment.RIGHT
            verticalAlignment (VerticalContentAlignment, Optional): Describes
                how the image should be aligned if it must be cropped or if
                using repeat fill mode. **_Defaults to None._** Allowed
                value(s):
                VerticalContentAlignment.TOP, VerticalContentAlignment.CENTER,
                or VerticalContentAlignment.BOTTOM
        """
        # Check types
        validate_uri(
            url,
        )

        validate_input(
            fillMode,
            OPTIONS.ImageFillMode,
            optional=True,
        )

        validate_input(
            horizontalAlignment,
            OPTIONS.HorizontalAlignment,
            optional=True,
        )

        validate_input(
            verticalAlignment,
            OPTIONS.VerticalContentAlignment,
            optional=True,
        )

        # Set properties
        self.url = url
        self.fillMode = fillMode
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment

        super().__init__(
            serializable_properties=[],
            simple_properties=[
                "url",
                "fillMode",
                "horizontalAlignment",
                "verticalAlignment",
            ],
        )
