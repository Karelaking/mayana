"""timeing returns the exequetion time of the given function"""

from time import perf_counter
from functools import wraps
from typing import Callable, Any


def get_time():
    """
    get time calculates the running time of the given function and print it to the terminal
    :param func: Function to find the run time
    :return: Return the run time of given function
    """
    def decorator(func:Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:

            # Note that timing your code once isn't the most reliable option
            # for timing your code. Look into the timeit module for more accurate
            # timing.

            start_time: float = perf_counter()
            result: Any = func(*args, **kwargs)
            end_time: float = perf_counter()

            print(f"{func.__name__}() - Ran in time {end_time - start_time:.10f} seconds.")
            return result

        return wrapper
    return decorator



