#!/usr/bin/env python3
"""
Basic annotations - sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of floats and ints"""
    return sum(mxd_lst)
