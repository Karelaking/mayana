from functools import wraps
from typing import Callable, Any
from time import sleep
from mayana.decorators.timeing import get_time


def retry(retries: int | str = 3, delay: float | str = 1) -> Callable:
    """
    retry returns the callable function that runs the give function, give value of time.

    :rtype: object
    :param retries:
    :param delay:
    :return:
    """

    # Don't let the user use this decorator if they are high
    if int(retries) < 1 or float(delay) <= 0:
        raise ValueError('Are you high, mate?')

    def decorator(func: Callable) -> Callable:

        @get_time()
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, int(retries) + 1):  # 1 to retries + 1 since upper bound is exclusive
                try:
                    print(f'Running ({i}): {func.__name__}()')
                    func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == int(retries):
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {int(retries)} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        sleep(float(delay))  # Add a delay before running the next iteration

        return wrapper

    return decorator
