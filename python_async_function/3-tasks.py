#!/usr/bin/env python3
"""
Async basics - tasks module
"""
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Function that returns an asyncio.Task"""
    return Task(wait_random(max_delay))
