import logging
from functools import wraps
from typing import Callable

import aiohttp


def aiohttp_error_handler(func: Callable) -> Callable:
    """Handle AIOHTTP connection errors with a decorator.

    Args:
        func (Callable): The request-handling function.

    Returns:
        Callable: Decorated function.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            response = await func(*args, **kwargs)
        except aiohttp.ClientConnectorError as exc:
            logging.critical('Connection error: {exc}'.format(exc=exc))
        return response
    return wrapper
