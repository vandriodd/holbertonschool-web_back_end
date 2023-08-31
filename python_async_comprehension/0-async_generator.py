#!/usr/bin/env python3
"""
Async Comprehension - async_generator module
"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that loops 10 times, each time asynchronously wait 1 second"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
