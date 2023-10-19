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


from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class SnapshotClient(NamespacedClient):
    @query_params("master_timeout", "cluster_manager_timeout", "wait_for_completion")
    async def create(
        self,
        repository: Any,
        snapshot: Any,
        *,
        body: Optional[Any] = None,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
        wait_for_completion: Optional[Any],
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
        Creates a snapshot in a repository.


        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg body: The snapshot definition
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository, snapshot),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("master_timeout", "cluster_manager_timeout")
    async def delete(
        self,
        repository: Any,
        snapshot: Any,
        *,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Deletes a snapshot.


        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_snapshot", repository, snapshot),
            params=params,
            headers=headers,
        )

    @query_params(
        "ignore_unavailable",
        "include_repository",
        "index_details",
        "master_timeout",
        "cluster_manager_timeout",
        "verbose",
    )
    async def get(
        self,
        repository: Any,
        snapshot: Any,
        *,
        ignore_unavailable: Optional[Any],
        include_repository: Optional[Any],
        index_details: Optional[Any],
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Returns information about a snapshot.


        :arg repository: A repository name
        :arg snapshot: A comma-separated list of snapshot names
        :arg ignore_unavailable: Whether to ignore unavailable
            snapshots, defaults to false which means a SnapshotMissingException is
            thrown
        :arg include_repository: Whether to include the repository name
            in the snapshot info. Defaults to true.
        :arg index_details: Whether to include details of each index in
            the snapshot, if those details are available. Defaults to false.
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg verbose: Whether to show verbose snapshot info or only show
            the basic info found in the repository index blob
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_snapshot", repository, snapshot),
            params=params,
            headers=headers,
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def delete_repository(
        self,
        repository: Any,
        *,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Deletes a repository.


        :arg repository: Name of the snapshot repository to unregister.
            Wildcard (`*`) patterns are supported.
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg timeout: Explicit operation timeout
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_snapshot", repository),
            params=params,
            headers=headers,
        )

    @query_params("local", "master_timeout", "cluster_manager_timeout")
    async def get_repository(
        self,
        *,
        repository: Optional[Any] = None,
        local: Optional[Any],
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Returns information about a repository.


        :arg repository: A comma-separated list of repository names
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        return await self.transport.perform_request(
            "GET", _make_path("_snapshot", repository), params=params, headers=headers
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout", "verify")
    async def create_repository(
        self,
        repository: Any,
        *,
        body: Any,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
        timeout: Optional[Any],
        verify: Optional[Any],
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
        Creates a repository.


        :arg repository: A repository name
        :arg body: The repository definition
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg timeout: Explicit operation timeout
        :arg verify: Whether to verify the repository after creation
        """
        for param in (repository, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("master_timeout", "cluster_manager_timeout", "wait_for_completion")
    async def restore(
        self,
        repository: Any,
        snapshot: Any,
        *,
        body: Optional[Any] = None,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
        wait_for_completion: Optional[Any],
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
        Restores a snapshot.


        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg body: Details of what to restore
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, snapshot, "_restore"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("ignore_unavailable", "master_timeout", "cluster_manager_timeout")
    async def status(
        self,
        *,
        repository: Optional[Any] = None,
        snapshot: Optional[Any] = None,
        ignore_unavailable: Optional[Any],
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Returns information about the status of a snapshot.


        :arg repository: A repository name
        :arg snapshot: A comma-separated list of snapshot names
        :arg ignore_unavailable: Whether to ignore unavailable
            snapshots, defaults to false which means a SnapshotMissingException is
            thrown
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_snapshot", repository, snapshot, "_status"),
            params=params,
            headers=headers,
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def verify_repository(
        self,
        repository: Any,
        *,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Verifies a repository.


        :arg repository: A repository name
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg timeout: Explicit operation timeout
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_verify"),
            params=params,
            headers=headers,
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def cleanup_repository(
        self,
        repository: Any,
        *,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Removes stale data from repository.


        :arg repository: A repository name
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg timeout: Explicit operation timeout
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_cleanup"),
            params=params,
            headers=headers,
        )

    @query_params("master_timeout", "cluster_manager_timeout")
    async def clone(
        self,
        repository: Any,
        snapshot: Any,
        target_snapshot: Any,
        *,
        body: Any,
        master_timeout: Optional[Any],
        cluster_manager_timeout: Optional[Any],
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
        Clones indices from one snapshot into another snapshot in the same repository.


        :arg repository: A repository name
        :arg snapshot: The name of the snapshot to clone from
        :arg target_snapshot: The name of the cloned snapshot to create
        :arg body: The snapshot clone definition
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        for param in (repository, snapshot, target_snapshot, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository, snapshot, "_clone", target_snapshot),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "blob_count",
        "concurrency",
        "detailed",
        "early_read_node_count",
        "max_blob_size",
        "max_total_data_size",
        "rare_action_probability",
        "rarely_abort_writes",
        "read_node_count",
        "seed",
        "timeout",
    )
    async def rrepository_analyze(
        self,
        repository: Any,
        *,
        blob_count: Optional[Any],
        concurrency: Optional[Any],
        detailed: Optional[Any],
        early_read_node_count: Optional[Any],
        max_blob_size: Optional[Any],
        max_total_data_size: Optional[Any],
        rare_action_probability: Optional[Any],
        rarely_abort_writes: Optional[Any],
        read_node_count: Optional[Any],
        seed: Optional[Any],
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
        Analyzes a repository for correctness and performance


        :arg repository: A repository name
        :arg blob_count: Number of blobs to create during the test.
            Defaults to 100.
        :arg concurrency: Number of operations to run concurrently
            during the test. Defaults to 10.
        :arg detailed: Whether to return detailed results or a summary.
            Defaults to 'false' so that only the summary is returned.
        :arg early_read_node_count: Number of nodes on which to perform
            an early read on a blob, i.e. before writing has completed. Early reads
            are rare actions so the 'rare_action_probability' parameter is also
            relevant. Defaults to 2.
        :arg max_blob_size: Maximum size of a blob to create during the
            test, e.g '1gb' or '100mb'. Defaults to '10mb'.
        :arg max_total_data_size: Maximum total size of all blobs to
            create during the test, e.g '1tb' or '100gb'. Defaults to '1gb'.
        :arg rare_action_probability: Probability of taking a rare
            action such as an early read or an overwrite. Defaults to 0.02.
        :arg rarely_abort_writes: Whether to rarely abort writes before
            they complete. Defaults to 'true'.
        :arg read_node_count: Number of nodes on which to read a blob
            after writing. Defaults to 10.
        :arg seed: Seed for the random number generator used to create
            the test workload. Defaults to a random value.
        :arg timeout: Explicit operation timeout. Defaults to '30s'.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_analyze"),
            params=params,
            headers=headers,
        )
