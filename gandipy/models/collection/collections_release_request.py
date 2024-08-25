# This file was generated by liblab | https://liblab.com/

from ..utils.json_map import JsonMap
from ..base import BaseModel


@JsonMap({"collection_name": "collectionName"})
class CollectionReleaseRequest(BaseModel):
    """CollectionReleaseRequest



    :param collection_name: collection_name
    :type collection_name: str
    """

    def __init__(self, collection_name: str, project_id: str):
        self.collection_name = collection_name
        self.project_id = project_id
