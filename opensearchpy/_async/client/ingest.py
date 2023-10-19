# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


# ----------------------------------------------------
# THIS CODE IS GENERATED AND MANUAL EDITS WILL BE LOST.
#
# To contribute, kindly make essential modifications through either the "opensearch-py client generator":
# https://github.com/opensearch-project/opensearch-py/blob/main/utils/generate-api.py
# or the "OpenSearch API specification" available at:
# https://github.com/opensearch-project/opensearch-api-specification/blob/main/OpenSearch.openapi.json
# -----------------------------------------------------


from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IngestClient(NamespacedClient):
    @query_params("cluster_manager_timeout", "master_timeout")
    async def get_pipeline(
        self,
        *,
        id: Optional[Any] = None,
        cluster_manager_timeout: Optional[Any],
        master_timeout: Optional[Any],
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Returns a pipeline.


        :arg id: Comma-separated list of pipeline ids. Wildcards
            supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_ingest", "pipeline", id), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def put_pipeline(
        self,
        id: Any,
        *,
        body: Any,
        cluster_manager_timeout: Optional[Any],
        master_timeout: Optional[Any],
        timeout: Optional[Any],
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Creates or updates a pipeline.


        :arg id: Pipeline ID.
        :arg body: The ingest definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def delete_pipeline(
        self,
        id: Any,
        *,
        cluster_manager_timeout: Optional[Any],
        master_timeout: Optional[Any],
        timeout: Optional[Any],
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Deletes a pipeline.


        :arg id: Pipeline ID.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
        )

    @query_params("verbose")
    async def simulate(
        self,
        *,
        body: Any,
        id: Optional[Any] = None,
        verbose: Optional[Any],
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Allows to simulate a pipeline with example documents.


        :arg body: The simulate definition
        :arg id: Pipeline ID.
        :arg verbose: Verbose mode. Display data output for each
            processor in executed pipeline.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_ingest", "pipeline", id, "_simulate"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def processor_grok(
        self,
        *,
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Returns a list of the built-in patterns.

        """
        return await self.transport.perform_request(
            "GET", "/_ingest/processor/grok", params=params, headers=headers
        )
