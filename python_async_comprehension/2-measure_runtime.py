#!/usr/bin/env python3
"""
Async Comprehension - measure_runtime module
"""
from time import perf_counter
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension four times in parallel"""
    start = perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = perf_counter()
    elapsed_time = end - start
    return elapsed_time
