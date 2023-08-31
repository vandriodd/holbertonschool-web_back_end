"""
Async Comprehension - async_generator module
"""
from asyncio import sleep
from random import uniform


async def async_generator():
    """Coroutine that loops 10 times, each time asynchronously wait 1 second"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
