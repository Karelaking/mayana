from typing import Callable, Any

def retry(retries:int | str = 3, delay:float | str = 1) -> Callable:
    """
    retry returns the callable function that runs the give function, give value of time.

    :rtype: object
    :param retries:
    :param delay:
    :return:
    """
