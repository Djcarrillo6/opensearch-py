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

import logging
from typing import (
    Any,
    AsyncGenerator,
    AsyncIterable,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

from ...serializer import Serializer
from ..client import AsyncOpenSearch

logger: logging.Logger

T = TypeVar("T")

def _chunk_actions(
    actions: Any, chunk_size: int, max_chunk_bytes: int, serializer: Serializer
) -> AsyncGenerator[Any, None]: ...
def _process_bulk_chunk(
    client: AsyncOpenSearch,
    bulk_actions: Any,
    bulk_data: Any,
    raise_on_exception: bool = ...,
    raise_on_error: bool = ...,
    ignore_status: Optional[Union[int, Collection[int]]] = ...,
    *args: Any,
    **kwargs: Any
) -> AsyncGenerator[Tuple[bool, Any], None]: ...
def aiter(x: Union[Iterable[T], AsyncIterable[T]]) -> AsyncGenerator[T, None]: ...
def azip(
    *iterables: Union[Iterable[T], AsyncIterable[T]]
) -> AsyncGenerator[Tuple[T, ...], None]: ...
def async_streaming_bulk(
    client: AsyncOpenSearch,
    actions: Union[Iterable[Any], AsyncIterable[Any]],
    chunk_size: int = ...,
    max_chunk_bytes: int = ...,
    raise_on_error: bool = ...,
    expand_action_callback: Callable[[Any], Tuple[Dict[str, Any], Optional[Any]]] = ...,
    raise_on_exception: bool = ...,
    max_retries: int = ...,
    initial_backoff: Union[float, int] = ...,
    max_backoff: Union[float, int] = ...,
    yield_ok: bool = ...,
    ignore_status: Optional[Union[int, Collection[int]]] = ...,
    *args: Any,
    **kwargs: Any
) -> AsyncGenerator[Tuple[bool, Any], None]: ...
async def async_bulk(
    client: AsyncOpenSearch,
    actions: Union[Iterable[Any], AsyncIterable[Any]],
    stats_only: bool = ...,
    ignore_status: Optional[Union[int, Collection[int]]] = ...,
    *args: Any,
    **kwargs: Any
) -> Tuple[int, Union[int, List[Any]]]: ...
def async_scan(
    client: AsyncOpenSearch,
    query: Optional[Any] = ...,
    scroll: str = ...,
    raise_on_error: bool = ...,
    preserve_order: bool = ...,
    size: int = ...,
    request_timeout: Optional[Union[float, int]] = ...,
    clear_scroll: bool = ...,
    scroll_kwargs: Optional[Mapping[str, Any]] = ...,
    **kwargs: Any
) -> AsyncGenerator[dict[str, Any], None]: ...
async def async_reindex(
    client: AsyncOpenSearch,
    source_index: Union[str, Collection[str]],
    target_index: str,
    query: Any = ...,
    target_client: Optional[AsyncOpenSearch] = ...,
    chunk_size: int = ...,
    scroll: str = ...,
    scan_kwargs: Optional[Mapping[str, Any]] = ...,
    bulk_kwargs: Optional[Mapping[str, Any]] = ...,
) -> Tuple[int, Union[int, List[Any]]]: ...
