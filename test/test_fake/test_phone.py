import unittest
import re
from parameterized import parameterized

from helper.fake.phone import (
    phone,
)  # Adjust import as needed


# Define a function to generate a large number of test cases
def generate_test_cases():
    formats = [
        "XXX-XXX-XXXX",
        "(XXX) XXX-XXXX",
        "XXX.XXX.XXXX",
        "XXX XXX XXXX",
        "+X-XXX-XXX-XXXX",
        "+ZZ-XX-XXXX-XXXX",
        "NXX-XXX-XXXX",
        "ZZZ-XX-XXXX",
        "XXX-XXXX",
        "XXX-XXX-XX",
        "+XXX (XX) XXXX XXXX",
        "XXX-XX-XX",
        "XX-XX-XX-XX",
        "XXXXX",
        "XXX-XX-XXX",
        "XX.XX.XX.XX",
        "+XX.XX.XXXX.XXXX",
    ]

    test_cases = []
    for fmt in formats:
        for _ in range(10):  # Create multiple test cases for each format
            test_cases.append((fmt,))
    return test_cases


class TestPhoneNumberGenerator(unittest.TestCase):

    @parameterized.expand(generate_test_cases())
    def test_phone_number_format(self, format_string):
        phone_number = phone(format_string)

        # Build the regex pattern based on the format string
        pattern = (
            re.escape(format_string)
            .replace("X", r"\d")
            .replace("N", r"[2-9]")
            .replace("Z", r"\d")
        )
        regex = f"^{pattern}$"

        self.assertTrue(
            re.match(regex, phone_number), f"Failed for format: {format_string}"
        )


if __name__ == "__main__":
    unittest.main()
