from random import shuffle
from typing import Generator, final
import re
import random
import string
from datetime import datetime, timedelta

from mayana.fake.states import loader
from utils.loader import Loader

from numpy.random import choice
loader = Loader()

class Password:
    def __init__(self, count: int = 1):
        self.__count: int = count

    def _generate_password(self):
        ...

    def password(self) -> Generator:
        ...

    @property
    def get_password(self):
        ...

    @property
    def get_lower_case_password(self):
        ...

    @property
    def get_upper_case_password(self):
        ...

    @property
    def get_digits_password(self):
        ...

    @property
    def get_punctuation_password(self):
        ...


# =====================================================================================================

class DOB:
    def __init__(self, count: int = 1):
        self.__count: int = count
        self.__start_data = "1980-01-01"
        self.__end_data = "2000-12-31"
        self.__date_format: str = "%Y-%m-%d"

    def _generate_dob(self, _start_date: str, _end_date: str, _date_format: str):

        # Convert start_date and end_date to datetime objects
        start_dt = datetime.strptime(_start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(_end_date, "%Y-%m-%d")

        # Generate a random date between start_dt and end_dt
        random_dt = start_dt + timedelta(days=random.randint(0, (end_dt - start_dt).days))

        # Convert the random date to the specified format
        dob_str = random_dt.strftime(_date_format)

        # Use regex to validate the date format
        # Regex pattern for validating different date formats
        regex_patterns = {
            "%Y-%m-%d": r"\d{4}-\d{2}-\d{2}",
            "%d/%m/%Y": r"\d{2}/\d{2}/\d{4}",
            "%m-%d-%Y": r"\d{2}-\d{2}-\d{4}",
            "%d-%b-%Y": r"\d{2}-[A-Za-z]{3}-\d{4}",
            "%B %d, %Y": r"[A-Za-z]+ \d{2}, \d{4}",
            "%d-%B-%Y": r"\d{2}-[A-Za-z]+-\d{4}",
            "%b %d, %Y": r"[A-Za-z]{3} \d{2}, \d{4}",
            "%d %b %Y": r"\d{2} [A-Za-z]{3} \d{4}",
            "%d %B %Y": r"\d{2} [A-Za-z]+ \d{4}",
            "%Y/%m/%d": r"\d{4}/\d{2}/\d{2}",
            "%Y.%m.%d": r"\d{4}\.\d{2}\.\d{2}",
            "%m/%d/%Y": r"\d{2}/\d{2}/\d{4}",
            "%m.%d.%Y": r"\d{2}\.\d{2}\.\d{4}",
        }

        # Get the appropriate regex pattern for the specified format
        if self.__date_format not in regex_patterns:
            raise ValueError("Unsupported date format.")

        date_pattern = re.compile(regex_patterns[_date_format])

        # Validate the generated date string against the regex pattern
        if not re.match(date_pattern, dob_str):
            raise ValueError("Generated date does not match the expected format.")
        return dob_str

    def dob(self, _start_date: str | None = None, _end_date: str | None = None, _date_format: str | None =
    None) -> Generator:
        if not _start_date:
            _start_date = self.__start_data
        if not _end_date:
            _end_date = self.__end_data
        if not _date_format:
            _date_format = self.__date_format

        for _ in range(self.__count):
            yield self._generate_dob(_start_date=_start_date, _end_date=_end_date, _date_format=_date_format)

    @property
    def get_dob(self):
        for _ in range(self.__count):
            yield self._generate_dob(_start_date=self.__start_data, _end_date=self.__end_data,
                                     _date_format=self.__date_format)


# =============================================================================================================================

gen = (item for item in range(3))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
