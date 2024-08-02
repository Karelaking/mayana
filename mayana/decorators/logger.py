import functools
import logging
import timeit
import cProfile
import pstats
from io import StringIO
from turtle import clear

logging.basicConfig(level=logging.DEBUG)


def logger(
    logger=None,
    level=logging.INFO,
    log_exceptions=True,
    reraise_exceptions=True,
    log_execution_time=True,
    profile_function=False,
):
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if logger.isEnabledFor(level):
                logger.log(
                    level, f"Calling {func.__name__}() with args={args}, kwargs={kwargs}"
                )

            start_time = timeit.default_timer() if log_execution_time else None

            if profile_function:
                profiler = cProfile.Profile()
                profiler.enable()

            try:
                result = func(*args, **kwargs)
                if logger.isEnabledFor(level):
                    logger.log(level, f"{func.__name__}() returned {result}")
                return result
            except Exception as e:
                if log_exceptions and logger.isEnabledFor(logging.ERROR):
                    logger.error(f"Exception in {func.__name__}(): {e}", exc_info=True)
                if reraise_exceptions:
                    raise
                return None
            finally:
                if log_execution_time and start_time is not None:
                    elapsed_time = timeit.default_timer() - start_time
                    logger.log(
                        level, f"{func.__name__}() took {elapsed_time:.4f} seconds"
                    )

                if profile_function:
                    profiler.disable()
                    s = StringIO()
                    ps = pstats.Stats(profiler, stream=s).sort_stats(
                        pstats.SortKey.CUMULATIVE
                    )
                    ps.print_stats()
                    logger.log(
                        level, f"Profile data for {func.__name__}():\n{s.getvalue()}"
                    )

        return wrapper

    return decorator


