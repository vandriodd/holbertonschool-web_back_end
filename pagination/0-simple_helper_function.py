#!/usr/bin/env python3
"""
Pagination - simple_helper_function module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
