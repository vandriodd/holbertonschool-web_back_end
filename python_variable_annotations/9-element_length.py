#!/usr/bin/env python3
"""
Basic annotations - element_length module
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and length"""
    return [(i, len(i)) for i in lst]
