from typing import List
from random import randint
import re

# Define patterns for different placeholders
patterns = {
    "X": lambda: str(randint(0, 9)),
    "N": lambda: str(randint(2, 9)),  # For non-zero leading digit area codes
    "Z": lambda: str(randint(1, 9)),  # For country codes
}


# Generate the phone number based on the format string
def generate_random_phone(format_string: str, patterns: dict) -> str:
    phone_number = ""
    for char in format_string:
        if char in patterns:
            phone_number += patterns[char]()
        else:
            phone_number += char
    return phone_number


def phone(format_string: str = "+ZZ XXX-XXX-XXXX", count: int = 1) -> str | List[str]:

    if count != 1:
        return [
            generate_random_phone(format_string=format_string, patterns=patterns)
            for _ in range(count)
        ]

    else:
        return generate_random_phone(format_string=format_string, patterns=patterns)


if __name__ == "__main__":
    print(phone())

# Example usage
# formats = [
#     "XXX-XXX-XXXX",
#     "(XXX) XXX-XXXX",
#     "XXX.XXX.XXXX",
#     "XXX XXX XXXX",
#     "+X-XXX-XXX-XXXX",
#     "+XX-XXXX-XXXX",
#     "+Z-XX-XXX-XXX-XXXX",
#     "+ZZ-XX-XXXX-XXXX",
# ]
#
