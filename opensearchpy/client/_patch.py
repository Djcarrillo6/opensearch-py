# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import warnings
from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from .utils import SKIP_IN_PATH, query_params


@query_params()
def list_all_point_in_time(
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
    Returns the list of active point in times searches

    .. warning::

    This API will be removed in a future version
    Use 'get_all_pits' API instead.

    """
    warnings.warn(
        "The 'list_all_point_in_time' API is deprecated and will be removed in a future version. Use 'get_all_pits' API instead.",
        DeprecationWarning,
    )

    return self.get_all_pits(params=params, headers=headers)


@query_params(
    "expand_wildcards", "ignore_unavailable", "keep_alive", "preference", "routing"
)
def create_point_in_time(
    self,
    *,
    index: Optional[Any],
    expand_wildcards: Optional[Any],
    ignore_unavailable: Optional[Any],
    keep_alive: Optional[Any],
    preference: Optional[Any],
    routing: Optional[Any],
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
    Create a point in time that can be used in subsequent searches


    :arg index: A comma-separated list of index names to open point
        in time; use `_all` or empty string to perform the operation on all
        indices
    :arg expand_wildcards: Whether to expand wildcard expression to
        concrete indices that are open, closed or both.  Valid choices: open,
        closed, hidden, none, all  Default: open
    :arg ignore_unavailable: Whether specified concrete indices
        should be ignored when unavailable (missing or closed)
    :arg keep_alive: Specific the time to live for the point in time
    :arg preference: Specify the node or shard the operation should
        be performed on (default: random)
    :arg routing: Specific routing value

    .. warning::

    This API will be removed in a future version
    Use 'create_pit' API instead.

    """
    warnings.warn(
        "The 'create_point_in_time' API is deprecated and will be removed in a future version. Use 'create_pit' API instead.",
        DeprecationWarning,
    )

    return self.create_pit(index=index, params=params, headers=headers)


@query_params()
def delete_point_in_time(
    self,
    *,
    body: Optional[Any] = None,
    all: Optional[bool] = False,
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
    Delete a point in time


    :arg body: a point-in-time id to delete
    :arg all: set it to `True` to delete all alive point in time.

    .. warning::

    This API will be removed in a future version
    Use 'delete_all_pits' or 'delete_pit' API instead.

    """
    warnings.warn(
        "The 'delete_point_in_time' API is deprecated and will be removed in a future version. Use 'delete_all_pits' or 'delete_pit' API instead.",
        DeprecationWarning,
    )

    if all:
        return self.delete_all_pits(params=params, headers=headers)
    else:
        return self.delete_pit(body=body, params=params, headers=headers)


@query_params()
def health_check(
    self, params: Union[Any, None] = None, headers: Union[Any, None] = None
) -> Union[bool, Any]:
    """
    Checks to see if the Security plugin is up and running.

    .. warning::

    This API will be removed in a future version
    Use 'health' API instead.

    """
    warnings.warn(
        "The 'health_check' API in security client is deprecated and will be removed in a future version. Use 'health' API instead.",
        DeprecationWarning,
    )

    return self.health(params=params, headers=headers)


@query_params()
def update_audit_config(
    self, body: Any, params: Union[Any, None] = None, headers: Union[Any, None] = None
) -> Union[bool, Any]:
    """
    A PUT call updates the audit configuration.

    .. warning::

    This API will be removed in a future version
    Use 'update_audit_configuration' API instead.

    """
    warnings.warn(
        "The 'update_audit_config' API in security client is deprecated and will be removed in a future version. Use 'update_audit_configuration' API instead.",
        DeprecationWarning,
    )

    if body in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'body'.")

    return self.update_audit_configuration(params=params, headers=headers, body=body)
