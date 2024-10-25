#!/usr/bin/env python3
"""
Create a Cache class
"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


class Cache:
    def __init__(self, host'=localhost', port=6379, db=0):
        """
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: union[str, bytes, int, float]) -> str:
        """
        """
        r_key = str(uuid.uuid4())
        self.__redis.set(r_key, data)
        return r_key
