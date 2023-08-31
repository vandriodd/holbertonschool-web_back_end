#!/usr/bin/env python3
"""
Async Comprehension - async comprehension module
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that will collect 10 random numbers using an async for"""
    return [i async for i in async_generator()]
