#!/usr/bin/env python3
"""
Async basics - basic_async_syntax module
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits with a random delay by given int"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
