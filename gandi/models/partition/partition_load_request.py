# This file was generated by liblab | https://liblab.com/

from typing import List
from ..utils.json_map import JsonMap
from ..base import BaseModel


@JsonMap({"project_id": "projectId", "collection_name": "collectionName", "partition_names": "partitionNames"})
class PartitionLoadRequest(BaseModel):
    """PartitionLoadRequest

    :param project_id: project_id
    :type project_id: str
    :param collection_name: collection_name
    :type collection_name: str
    :param partition_names: partition_names
    :type partition_names: List[str]
    """

    def __init__(self, collection_name: str, host: str, partition_names: List[str], project_id: str):
        self.project_id = project_id
        self.collection_name = collection_name
        self.host = host
        self.partition_names = partition_names
