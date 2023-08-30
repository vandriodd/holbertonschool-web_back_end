#!/usr/bin/env python3
"""
Basic annotations - to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of k and v squared"""
    return (k, v**2)
