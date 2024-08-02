# from itertools import count
import random
import re
from datetime import datetime, timedelta


def generate_random_dob(): ...


def dob(
    start_date: str = "1980-01-01",
    end_date: str = "2000-12-31",
    date_format: str = "%d-%b-%Y",
    count: int = 1,
) -> str | list[str]:
    """
    Generate a random date of birth between start_date and end_date in the specified format.

    :param start_date: The start date in 'YYYY-MM-DD' format.
    :param end_date: The end date in 'YYYY-MM-DD' format.
    :param date_format: The desired format of the output date string.
    :return: A string representing a random date of birth in the specified format.
    """



# # Example usage:
# start_date = "1980-01-01"
# end_date = "2000-12-31"
# date_format = "%d-%b-%Y"  # Example format

# print(type(dob(start_date, end_date, date_format)))
