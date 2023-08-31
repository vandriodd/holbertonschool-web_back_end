#!/usr/bin/env python3
"""
Async basics - basic_async_syntax module
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits with a random delay by given int"""
    await asyncio.sleep(uniform(0, max_delay))
    return uniform(0, max_delay)
