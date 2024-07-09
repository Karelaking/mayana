from typing import List
from random import randint
import re


def phone(format_string="+ZZ XXX-XXX-XXXX"):
    # Define patterns for different placeholders
    patterns = {
        "X": lambda: str(randint(0, 9)),
        "N": lambda: str(randint(2, 9)),  # For non-zero leading digit area codes
        "Z": lambda: str(randint(1, 9)),  # For country codes
    }

    # Generate the phone number based on the format string
    phone_number = ""
    for char in format_string:
        if char in patterns:
            phone_number += patterns[char]()
        else:
            phone_number += char

    return phone_number


# Example usage
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

print(phone())