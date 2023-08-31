#!/usr/bin/env python3
"""
Async basics - tasks module
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that returns a list of all delays"""
    delay_list = []
    for _ in range(n):
        delay_list.append(await task_wait_random(max_delay))
    return sorted(delay_list)
