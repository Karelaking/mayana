from secrets import choice
from random import shuffle
from pathlib import Path

from utils.pickler import Loader

loader: Loader = Loader()


class Name:
    def __init__(self, count: int = 1, country: str = "India"):
        self.__name_data = loader.load_data(file_path=str(Path.joinpath(Path(__file__).parent.parent.parent,
                                                                        "constants/name.json")))
        self.__name_parts_data = loader.load_data(file_path=str(Path.joinpath(Path(__file__).parent.parent.parent,
                                                                        "constants/name_parts.json")))
        # self.__name_data = loader.load_data(file_path="constants/name.json")
        # self.__name_parts_data = loader.load_data(file_path="constants/name_parts.json")
        self.count: int = count
        self.country: str = country

    def __iter__(self):
        yield self

    def __next__(self):
        """
        Returns the next item from the iterator.

        Raises:
            StopIteration: If there are no more items to return.
        """
        ...

    def _generate_name(self, first: bool, middel: bool, last: bool, suffix: bool, prefix: bool, title: bool,
                       country: str):
        __full_name: str = ""
        __title: str = self.__name_parts_data["title"]
        __prefix: str = self.__name_parts_data["prefix"]
        __first: str = self.__name_data[country]["first_names"]
        __middel: str = self.__name_data[country]["middle_names"]
        __last: str = self.__name_data[country]["last_names"]
        __suffix: str = self.__name_parts_data["suffix"]

        __full_name += choice(__title) if title else str()
        __full_name += " " + choice(__prefix) if prefix else str()
        __full_name += " " + choice(__first) if first else str()
        __full_name += " " + choice(__middel) if middel else str()
        __full_name += " " + choice(__last) if last else str()
        __full_name += choice(__suffix) if suffix else str()

        return __full_name.strip()

    def name(self, first: bool = True, middel: bool = False, last: bool = False, suffix: bool = False,
             prefix: bool = False, title: bool = False, country: str = "India"):

        for _ in range(self.count):
            yield self._generate_name(first=first, title=title, prefix=prefix, middel=middel, last=last, suffix=suffix,
                                      country=country)

    @property
    def get_name(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=False, first=True, middel=False, last=True, suffix=False,
                                      country=self.country)

    @property
    def get_first_name(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=False, first=True, middel=False, last=False, suffix=False,
                                      country=self.country)

    @property
    def get_last_name(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=False, first=False, middel=False, last=True, suffix=False,
                                      country=self.country)

    @property
    def get_name_with_title(self):
        for _ in range(self.count):
            yield self._generate_name(title=True, prefix=False, first=True, middel=False, last=True, suffix=False,
                                      country=self.country)

    @property
    def get_name_with_prefix(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=True, first=True, middel=False, last=True, suffix=False,
                                      country=self.country)

    @property
    def get_name_with_suffix(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=False, first=True, middel=False, last=True, suffix=True,
                                      country=self.country)

    @property
    def get_name_with_middel(self):
        for _ in range(self.count):
            yield self._generate_name(title=False, prefix=False, first=True, middel=True, last=True, suffix=False,
                                      country=self.country)
