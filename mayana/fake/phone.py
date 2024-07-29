from random import randint


class Phone:
    def __init__(self, count: int = 1):
        self.__count: int = count
        # Define patterns for different placeholders
        self.__patterns = {
            "X": lambda: str(randint(0, 9)),
            "N": lambda: str(randint(2, 9)),  # For non-zero leading digit area codes
            "Z": lambda: str(randint(1, 9)),  # For country codes
        }

    def _generate_phone(self, format_string: str) -> str:
        phone_number = ""
        for char in format_string:
            if char in self.__patterns:
                phone_number += self.__patterns[char]()
            else:
                phone_number += char
        return phone_number

    def phone(self, phone_format: str = "+ZZ XXX-XXX-XXXX"):
        """
        Generate a specified number of phone numbers in the given format.

        :param phone_format: The format for the phone numbers.
        :return: A generator of phone numbers.

        formats = [
            "XXX-XXX-XXXX",
            "(XXX) XXX-XXXX",
            "XXX.XXX.XXXX",
            "XXX XXX XXXX",
            "+X-XXX-XXX-XXXX",
            "+XX-XXXX-XXXX",
            "+Z-XX-XXX-XXX-XXXX",
            "+ZZ-XX-XXXX-XXXX",
        ]

        """
        for _ in range(self.__count):
            yield self._generate_phone(format_string=phone_format)

    @property
    def get_phone(self):
        for _ in range(self.__count):
            yield self._generate_phone(format_string="+ZZ XXX-XXX-XXXX")
