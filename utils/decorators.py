import time

from utils.logger import logger


def log_execution(func):

    def wrapper(
        *args,
        **kwargs
    ):

        start = time.time()

        logger.info(
            f"Started {func.__name__}"
        )

        result = func(
            *args,
            **kwargs
        )

        end = time.time()

        logger.info(
            f"Completed {func.__name__}"
        )

        logger.info(
            f"Execution Time: {end-start:.2f} sec"
        )

        return result

    return wrapper