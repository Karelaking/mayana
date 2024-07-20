import unittest
import re
from random import choice, randint
from mayana.fake.password import password  # Adjust import as needed


# Generate 100 different test cases
def generate_test_cases():
    test_cases = []
    for i in range(100):
        length = randint(8, 20)
        is_use_digits = choice([True, False])
        is_use_lower_case = choice([True, False])
        is_use_upper_case = choice([True, False])
        is_use_punctuation = choice([True, False])

        if not (
            is_use_digits
            or is_use_lower_case
            or is_use_upper_case
            or is_use_punctuation
        ):
            is_use_lower_case = True  # Ensure at least one character set is used

        name = f"test_case_{i+1}"

        # Create the regex pattern for validation
        pattern = "^"
        if is_use_digits:
            pattern += "(?=.*\\d)"
        if is_use_lower_case:
            pattern += "(?=.*[a-z])"
        if is_use_upper_case:
            pattern += "(?=.*[A-Z])"
        if is_use_punctuation:
            pattern += "(?=.*[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~])"
        pattern += ".{" + str(length) + "}$"

        test_cases.append(
            (
                name,
                length,
                is_use_digits,
                is_use_lower_case,
                is_use_upper_case,
                is_use_punctuation,
                pattern,
            )
        )
    return test_cases


class TestPasswordGenerator(unittest.TestCase):

    def __init__(
        self,
        methodName="runTest",
        case_name=None,
        length=None,
        is_use_digits=None,
        is_use_lower_case=None,
        is_use_upper_case=None,
        is_use_punctuation=None,
        pattern=None,
    ):
        super(TestPasswordGenerator, self).__init__(methodName)
        self.case_name = case_name
        self.length = length
        self.is_use_digits = is_use_digits
        self.is_use_lower_case = is_use_lower_case
        self.is_use_upper_case = is_use_upper_case
        self.is_use_punctuation = is_use_punctuation
        self.pattern = pattern

    def shortDescription(self):
        return f"{self.case_name}: len={self.length}, digits={self.is_use_digits}, lower={self.is_use_lower_case}, upper={self.is_use_upper_case}, punctuation={self.is_use_punctuation}"

    def test_generate_password(self):
        passwd = password(
            self.length,  # type: ignore
            self.is_use_digits,  # type: ignore
            self.is_use_lower_case,  # type: ignore
            self.is_use_upper_case,  # type: ignore
            self.is_use_punctuation,  # type: ignore
        )
        self.assertTrue(
            re.match(self.pattern, passwd), f"Failed for test case: {self.case_name}" # type: ignore
        )


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for (
        name,
        length,
        is_use_digits,
        is_use_lower_case,
        is_use_upper_case,
        is_use_punctuation,
        pattern,
    ) in generate_test_cases():
        test = TestPasswordGenerator(
            "test_generate_password",
            name,
            length,
            is_use_digits,
            is_use_lower_case,
            is_use_upper_case,
            is_use_punctuation,
            pattern,
        )
        suite.addTest(test)
    return suite


if __name__ == "__main__":
    unittest.main(
        testLoader=unittest.defaultTestLoader,
        testRunner=unittest.TextTestRunner(
            resultclass=unittest.TextTestResult, verbosity=2
        ),
    )
