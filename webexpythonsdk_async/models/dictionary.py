from typing import Union

from webexpythonsdk_async.utils import json_dict


def dict_data_factory(model: str, json_data: Union[dict, str]):
    return json_dict(json_data)
