from pathlib import Path
from random import choice
from typing import List

from utils.loader import Loader

loader: Loader = Loader()


class Name:
    """
    Generates a fake name based on a given name format string.
    """

    def __init__(self, count: int = 1, country: str = "India"):
        self.__name_data = loader.load_data(file_path=Path.joinpath(Path(__file__).parent.parent.parent,

                                                                    "constants/name.json"))
        self.__name_parts_data = loader.load_data(file_path=Path.joinpath(Path(__file__).parent.parent.parent,
                                                                          "constants/name_parts.json"))
        self.count: int = count
        self.country: str = country
        self._title: List[str] = self.__name_parts_data["title"]
        self._prefix: List[str] = self.__name_parts_data["prefix"]
        self._first: List[str] = self.__name_data[country]["first_names"]
        self._middel: List[str] = self.__name_data[country]["middle_names"]
        self._last: List[str] = self.__name_data[country]["last_names"]
        self._suffix: List[str] = self.__name_parts_data["suffix"]

    def __iter__(self):
        yield self

    def _generate_name(self, __name_format: str = "f M l", __count: int = 1) -> str:
        _patterns = {
            "t": lambda: choice(self._title).lower(),
            "p": lambda: choice(self._prefix).lower(),
            "f": lambda: choice(self._first).lower(),
            "m": lambda: choice(self._middel).lower(),
            "l": lambda: choice(self._last).lower(),
            "s": lambda: choice(self._suffix).lower(),
            "T": lambda: choice(self._title).capitalize(),
            "P": lambda: choice(self._prefix).capitalize(),
            "F": lambda: choice(self._first).capitalize(),
            "M": lambda: choice(self._middel).capitalize(),
            "L": lambda: choice(self._last).capitalize(),
            "S": lambda: choice(self._suffix).capitalize(),
        }

        _full_name: str = ""

        for char in __name_format:
            if char in _patterns:
                _full_name += _patterns[char]()
            else:
                _full_name += char
        return _full_name

    def name(self, name_format: str):
        for _ in range(self.count):
            yield self._generate_name(name_format)

    @property
    def get_name(self):
        for _ in range(self.count):
            yield self._generate_name("F L")

    @property
    def get_first_name(self):
        for _ in range(self.count):
            yield self._generate_name("F")

    @property
    def get_last_name(self):
        for _ in range(self.count):
            yield self._generate_name("L")

    @property
    def get_name_with_title(self):
        for _ in range(self.count):
            yield self._generate_name("T F L")

    @property
    def get_name_with_prefix(self):
        for _ in range(self.count):
            yield self._generate_name("P F L")

    @property
    def get_name_with_suffix(self):
        for _ in range(self.count):
            yield self._generate_name("F L S")

    @property
    def get_name_with_middel(self):
        for _ in range(self.count):
            yield self._generate_name("F M L")
