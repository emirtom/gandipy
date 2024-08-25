# This file was generated by liblab | https://liblab.com/

from typing import Union
from typing import List
from ..utils.json_map import JsonMap
from ..base import BaseModel
from ..base import OneOfBaseModel
import pandas as pd


class VectorsInsertRequestDataGuard(OneOfBaseModel):
    class_list = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "List[str]": List[str],
        "List[int]": List[int],
        "List[float]": List[float],
        "List[bool]": List[bool],
    }


VectorsInsertRequestData = Union[
    str, int, float, bool, List[str], List[int], List[float], List[bool]
]


@JsonMap(
    {
        "collection_name": "collectionName",
        "partition_name": "partitionName",
    }
)
class VectorsInsertRequest(BaseModel):
    """VectorsInsertRequest



    :param collection_name: collection_name
    :type collection_name: str
    :param partition_name: partition_name, defaults to None
    :type partition_name: str, optional
    :param data: data, defaults to None
    :type data: dict, optional
    """

    def __init__(
        self,
        collection_name: str,
        project_id: str,
        partition_name: str = None,
        data=None,
    ):
        self.collection_name = collection_name
        if partition_name is not None:
            self.partition_name = partition_name
        if data is not None:
            if isinstance(data, pd.DataFrame):
                data = data.to_dict(orient="records")
            self.data = data
        self.project_id = project_id
