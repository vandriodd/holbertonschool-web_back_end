#!/usr/bin/env python3
"""
Basic annotations (advanced) - safe_first_element module
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
