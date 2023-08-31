#!/usr/bin/env python3
"""
Async basics - concurrent_coroutines module
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that returns a list of all delays"""
    delays_list = []
    for _ in range(n):
        delays_list.append(await wait_random(max_delay))
    return sorted(delays_list)
