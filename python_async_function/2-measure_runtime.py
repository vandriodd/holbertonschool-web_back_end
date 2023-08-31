#!/usr/bin/env python3
"""
Async basics - measure_runtime module
"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the total execution time"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    elapsed_time = end - start
    return elapsed_time / n
