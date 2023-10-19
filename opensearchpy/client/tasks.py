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


import warnings
from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class TasksClient(NamespacedClient):
    @query_params(
        "actions",
        "detailed",
        "group_by",
        "nodes",
        "parent_task_id",
        "timeout",
        "wait_for_completion",
    )
    def list(
        self,
        *,
        actions: Optional[Any],
        detailed: Optional[Any],
        group_by: Optional[Any],
        nodes: Optional[Any],
        parent_task_id: Optional[Any],
        timeout: Optional[Any],
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
        Returns a list of tasks.


        :arg actions: Comma-separated list of actions that should be
            returned. Leave empty to return all.
        :arg detailed: Return detailed task information.
        :arg group_by: Group tasks by nodes or parent/child
            relationships.  Valid choices: nodes, parents, none
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Return tasks with specified parent task id
            (node_id:task_number). Set to -1 to return all.
        :arg timeout: Operation timeout.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning.
        """
        return self.transport.perform_request(
            "GET", "/_tasks", params=params, headers=headers
        )

    @query_params("actions", "nodes", "parent_task_id", "wait_for_completion")
    def cancel(
        self,
        *,
        task_id: Optional[Any] = None,
        actions: Optional[Any],
        nodes: Optional[Any],
        parent_task_id: Optional[Any],
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
        Cancels a task, if it can be cancelled through an API.


        :arg task_id: Cancel the task with specified task id
            (node_id:task_number).
        :arg actions: Comma-separated list of actions that should be
            cancelled. Leave empty to cancel all.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Cancel tasks with specified parent task id
            (node_id:task_number). Set to -1 to cancel all.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_tasks", task_id, "_cancel"),
            params=params,
            headers=headers,
        )

    @query_params("timeout", "wait_for_completion")
    def get(
        self,
        *,
        task_id: Optional[Any] = None,
        timeout: Optional[Any],
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
        Returns information about a task.


        :arg task_id: Return the task with specified id
            (node_id:task_number).
        :arg timeout: Operation timeout.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning.
        """
        if task_id in SKIP_IN_PATH:
            warnings.warn(
                "Calling client.tasks.get() without a task_id is deprecated "
                "and will be removed in v8.0. Use client.tasks.list() instead.",
                category=DeprecationWarning,
                stacklevel=3,
            )

        return self.transport.perform_request(
            "GET", _make_path("_tasks", task_id), params=params, headers=headers
        )
