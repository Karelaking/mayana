from typing import List, Any
from random import choice


class PlaceHolder:
    def __init__(self, count: int = 1):
        self.__count: int = count

    def __iter__(self):
        yield self

    def __next__(self):
        """
        Returns the next item from the iterator.

        Raises:
            StopIteration: If there are no more items to yield.
        """
        ...

    @staticmethod
    def _generate_placeholder(_placeholders):
        placeholder = choice(_placeholders)
        return placeholder

    def placeholder(self, __placeholder: List[Any]):
        for _ in range(self.__count):
            yield self._generate_placeholder(_placeholders=__placeholder)

    @property
    def get_placeholder(self):
        for _ in range(self.__count):
            yield self._generate_placeholder(_placeholders=["None"])
