from webexpythonsdk_async.models.cards.adaptive_card_component import (
    AdaptiveCardComponent,
)
import webexpythonsdk_async.models.cards.card_elements as CARD_ELEMENTS
import webexpythonsdk_async.models.cards.containers as CONTAINERS
import webexpythonsdk_async.models.cards.actions as ACTIONS
import webexpythonsdk_async.models.cards.inputs as INPUTS
import webexpythonsdk_async.models.cards.types as TYPES
import webexpythonsdk_async.models.cards.options as OPTIONS
from webexpythonsdk_async.models.cards.utils import (
    check_type,
    validate_input,
    validate_uri,
)


class AdaptiveCard(AdaptiveCardComponent):
    """
    **Adaptive Card - Adaptive Card Element**

    An Adaptive Card, containing a free-form body of card elements, and an
    optional set of actions.

    **_Note:_** Webex currently supports version 1.3 of adaptive cards and
    thus only features from that release are supported in this abstraction.
    """

    type = "AdaptiveCard"
    schema = "http://adaptivecards.io/schemas/adaptive-card.json"
    version = "1.3"

    def __init__(
        self,
        body: list[object] = None,
        actions: list[object] = None,
        selectAction: object = None,
        fallbackText: str = None,
        backgroundImage: object = None,
        minHeight: str = None,
        speak: str = None,
        lang: str = None,
        verticalContentAlignment: OPTIONS.VerticalContentAlignment = None,
    ):
        """
        Initialize a new Adaptive Card element.

        Args:
            body (list of Card Element(s), Optional): The card elements to
                show in the primary card region. **_Defaults to None._**
                Allowed value(s):
                ActionSet, ColumnSet, Container, FactSet, Image, ImageSet,
                ChoiceSet, Date, Number, Text, Time, Toggle, Media,
                RichTextBlock, TextBlock
            actions (list of Actions Element(s), Optional): The Actions to
                show in the card's action bar. **_Defaults to None._** Allowed
                value(s):
                OpenUrl, ShowCard, Submit, ToggleVisibility
            selectAction (Actions Element, Optional): An Action that will be
                invoked when the card is tapped or selected. Action.ShowCard
                is not supported. **_Defaults to None._** Allowed value(s):
                OpenUrl, Submit, or ToggleVisibility
            fallbackText (str, Optional): Text shown when the client doesn't
                support the version specified (may contain markdown).
                **_Defaults to None._**
            backgroundImage (BackgroundImage or uri, Optional): Specifies the
                background image of the card. **_Defaults to None._** Allowed
                value(s):
                BackgroundImage or uri
            minHeight (str, Optional): Specifies the minimum height of the
                card. **_Defaults to None._**
            speak (str, Optional): Specifies what should be spoken for this
                entire card. This is simple text or SSML fragment. **_Defaults
                to None._**
            lang (str, Optional): The 2-letter ISO-639-1 language used in the
                card. Used to localize any date/time functions. **_Defaults to
                None._**
            verticalContentAlignment (VerticalContentAlignment, Optional):
                Defines how the content should be aligned vertically within
                the container. Only relevant for fixed-height cards, or cards
                with a minHeight specified. **_Defaults to None._** Allowed
                value(s):
                VerticalContentAlignment.TOP, VerticalContentAlignment.CENTER,
                or VerticalContentAlignment.BOTTOM

        """
        # Check types
        check_type(
            body,
            (
                CONTAINERS.ActionSet,
                CONTAINERS.ColumnSet,
                CONTAINERS.Container,
                CONTAINERS.FactSet,
                CARD_ELEMENTS.Image,
                CONTAINERS.ImageSet,
                INPUTS.ChoiceSet,
                INPUTS.Date,
                INPUTS.Number,
                INPUTS.Text,
                INPUTS.Time,
                INPUTS.Toggle,
                CARD_ELEMENTS.Media,
                CARD_ELEMENTS.RichTextBlock,
                CARD_ELEMENTS.TextBlock,
            ),
            optional=True,
            is_list=True,
        )

        check_type(
            actions,
            (
                ACTIONS.OpenUrl,
                ACTIONS.ShowCard,
                ACTIONS.Submit,
                ACTIONS.ToggleVisibility,
            ),
            optional=True,
            is_list=True,
        )

        check_type(
            selectAction,
            (
                ACTIONS.OpenUrl,
                ACTIONS.Submit,
                ACTIONS.ToggleVisibility,
            ),
            optional=True,
        )

        check_type(
            fallbackText,
            str,
            optional=True,
        )

        # Check if backgroundImage is of TYPES.BackgroundImage type
        if hasattr(backgroundImage, "to_dict"):
            check_type(
                backgroundImage,
                TYPES.BackgroundImage,
                optional=True,
            )
        # If not, check if it is an URI and reachable
        else:
            validate_uri(
                uri=backgroundImage,
                optional=True,
            )

        check_type(
            minHeight,
            str,
            optional=True,
        )

        check_type(
            speak,
            str,
            optional=True,
        )

        check_type(
            lang,
            str,
            optional=True,
        )

        check_type(
            verticalContentAlignment,
            str,
            optional=True,
        )

        validate_input(
            verticalContentAlignment,
            OPTIONS.VerticalContentAlignment,
            optional=True,
        )

        # Set properties
        self.body = body
        self.actions = actions
        self.selectAction = selectAction
        self.fallbackText = fallbackText
        self.backgroundImage = backgroundImage
        self.minHeight = minHeight
        self.speak = speak
        self.lang = lang
        self.verticalContentAlignment = verticalContentAlignment

        super().__init__(
            serializable_properties=[
                "body",
                "actions",
                "selectAction",
                *(["backgroundImage"] if hasattr(backgroundImage, "to_dict") else []),
            ],
            simple_properties=[
                "type",
                "version",
                "fallbackText",
                *([] if hasattr(backgroundImage, "to_dict") else ["backgroundImage"]),
                "minHeight",
                "speak",
                "lang",
                "verticalContentAlignment",
            ],
        )

    def to_dict(self):
        # We need to overwrite the to_dict method to add the $schema
        # property that can't be specified the normal way due to the
        # `$` in the property name.
        serialized_data = super().to_dict()
        serialized_data["$schema"] = self.schema
        return serialized_data
