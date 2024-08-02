import random
import string
import re
from typing import Generator


class PinCode:
    def __init__(self, count: int = 1):
        self.__count: int = count
        self.__length: int = 6

    @staticmethod
    def _generate_pincode(_length: int):
        if _length <= 0:
            raise ValueError("PIN length must be greater than zero.")

        # Regular expression to ensure the PIN consists only of digits
        pin_regex = re.compile(r"^\d+$")

        while True:
            # Generate a random PIN code using digits
            pin = "".join(random.choices(string.digits, k=_length))

            # Check if the generated PIN matches the regex (only digits)
            if pin_regex.match(pin):
                break

        return pin

    def pincode(self, lenght: int = 6) -> Generator:
        for _ in range(self.__count):
            yield self._generate_pincode(_length=lenght)

    @property
    def get_pincode(self):
        for _ in range(self.__count):
            yield self._generate_pincode(_length=self.__length)
