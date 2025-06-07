import json

from webexpythonsdk_async.utils import json_dict


class SimpleDataModel(object):
    """Model a Webex JSON object as a simple Python object."""

    def __init__(self, json_data):
        """Init a new SimpleDataModel object from a dictionary or JSON string.

        Args:
            json_data(dict, str): Input JSON string or dictionary.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        super(SimpleDataModel, self).__init__()
        for attribute, value in json_dict(json_data).items():
            setattr(self, attribute, value)

    def __str__(self):
        """A human-readable string representation of this object."""
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

    def __repr__(self):
        """A string representing this object as valid Python expression."""
        class_str = self.__class__.__name__
        json_str = json.dumps(self.__dict__, ensure_ascii=False)
        return "{}({})".format(class_str, repr(json_str))


def simple_data_factory(model, json_data):
    """Factory function for creating SimpleDataModel objects.

    Args:
        model(str): The data model to use when creating the data
            object (message, room, membership, etc.).
        json_data(str, dict): The JSON string or dictionary data with
            which to initialize the object.

    Returns:
        SimpleDataModel: The created SimpleDataModel object.

    Raises:
        TypeError: If the json_data parameter is not a JSON string or
            dictionary.

    """
    return SimpleDataModel(json_data)
