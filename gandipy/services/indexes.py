# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.index.index_request import IndexRequest, Index
from ..models.index.indexes_list_request import IndexListRequest
from ..models.index.indexes_drop_request import IndexDropRequest
from ..models.index.indexes_describe_request import IndexDescribeRequest


class IndexesService(BaseService):

    @cast_models
    def create(
        self,
        collection_name: str,
        index_params: List[Index] = None,
    ):
        """This creates a named index for a target field, which can either be a vector field or a scalar field.

        :param collection_name: The name of the collection.
        :type collection_name: str
        :param host: The host of the collection.
        :type host: str
        :param project_id: ID of the project where the collection is.

        :param index_params: List of indexes to creat inside the collection.
        :type index_params: List[Index]
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        """

        request_body = IndexRequest(
            collection_name=collection_name,
            project_id=self.project_id,
            index_params=index_params,
        )

        Validator(IndexRequest).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/indexes/create", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def describe(self, collection_name: str, index_name: str):
        """Returns the details of an index.

        :param collection_name: The name of the collection.
        :type collection_name: str
        :param index_name: The name of the index.
        :type index_name: str
        :param host: The host name.
        :type host: str
        :param project_id: ID of the project where the collection is.

        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        """

        request_body = IndexDescribeRequest(
            collection_name=collection_name,
            index_name=index_name,
            project_id=self.project_id,
        )

        Validator(IndexDescribeRequest).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/indexes/describe", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def drop(self, collection_name: str, index_name: str):
        """This operation drops index from a specified collection.

        :param collection_name: The name of the collection.
        :type collection_name: str
        :param index_name: The name of the index.
        :type index_name: str
        :param host: The host name.
        :type host: str
        :param project_id: ID of the project where the collection is.

        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        """

        request_body = IndexDropRequest(
            collection_name=collection_name,
            index_name=index_name,
            project_id=self.project_id,
        )

        Validator(IndexDropRequest).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/indexes/drop", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def list(self, collection_name: str):
        """Returns a list of all indexes in the specified collection.

        :param collection_name: The name of the collection.
        :type collection_name: str
        :param host: The host name.
        :type host: str
        :param project_id: ID of the project where the collection is.

        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        """

        request_body = IndexListRequest(
            collection_name=collection_name,
            project_id=self.project_id,
        )

        Validator(IndexListRequest).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/indexes/list", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response
