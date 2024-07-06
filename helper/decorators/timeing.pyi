from typing import Callable, Any

def get_time() -> Callable:
    """
    get time calculates the running time of the given function and print it to the terminal
    :param func: Function to find the run time
    :return: Return the run time of given function
    """

    def wrapper(*args, **kwargs) -> Any: ...