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


import sys
from typing import Callable, Tuple, Type, Union

PY2: bool = sys.version_info[0] == 2

if PY2:
    string_types = (basestring,)  # noqa: F821
    from itertools import imap as map
    from urllib import quote, quote_plus, unquote, urlencode

    from Queue import Queue
    from urlparse import urlparse

    def to_str(x, encoding="ascii"):
        if not isinstance(x, str):
            return x.encode(encoding)
        return x

    to_bytes: Callable[[Union[str, bytes]], bytes] = to_str

else:
    string_types = str, bytes
    from urllib.parse import quote, quote_plus, unquote, urlencode, urlparse

    map = map
    from queue import Queue

    def to_str(x, encoding="ascii"):
        if not isinstance(x, str):
            return x.decode(encoding)
        return x

    def to_bytes(x, encoding="ascii"):
        if not isinstance(x, bytes):
            return x.encode(encoding)
        return x


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


try:
    reraise_exceptions: Tuple[Type[Exception], ...] = (RecursionError,)
except NameError:
    reraise_exceptions = ()

try:
    import asyncio

    reraise_exceptions += (asyncio.CancelledError,)
except (ImportError, AttributeError):
    pass


__all__ = [
    "string_types",
    "reraise_exceptions",
    "quote_plus",
    "quote",
    "urlencode",
    "unquote",
    "urlparse",
    "map",
    "Queue",
    "Mapping",
]
