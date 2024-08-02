from pathlib import Path
from random import shuffle, choice
from typing import Generator, List, Dict

from utils.loader import Loader

loader: Loader = Loader()


class Country:
    def __init__(self, count: int = 1):
        self.__count: int = count
        self.__countries_data: Dict[str, List[str]] = loader.load_data(file_path=Path.joinpath(Path(
            __file__).parent.parent.parent,
                                                                         "constants/country.json"))

    def __iter__(self):
        return self

    def _generate_country(self) -> str:
        shuffle(self.__countries_data["Country"])
        country = choice(self.__countries_data["Country"])
        return country

    @property
    def get_country(self) -> Generator:
        for _ in range(self.__count):
            yield self._generate_country()
