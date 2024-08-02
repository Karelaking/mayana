import datetime
import unittest
from parameterized import parameterized
import re
from datetime import datetime
from mayana.fake.dob import generate_random_dob


class TestGenerateRandomDOB(unittest.TestCase):
    @parameterized.expand(
        [
            ("1980-01-01", "2000-12-31", "%Y-%m-%d", r"\d{4}-\d{2}-\d{2}"),
            ("1980-01-01", "2000-12-31", "%d/%m/%Y", r"\d{2}/\d{2}/\d{4}"),
            ("1980-01-01", "2000-12-31", "%m-%d-%Y", r"\d{2}-\d{2}-\d{4}"),
            ("1980-01-01", "2000-12-31", "%d-%b-%Y", r"\d{2}-[A-Za-z]{3}-\d{4}"),
            ("1980-01-01", "2000-12-31", "%B %d, %Y", r"[A-Za-z]+ \d{2}, \d{4}"),
            ("1980-01-01", "2000-12-31", "%d-%B-%Y", r"\d{2}-[A-Za-z]+-\d{4}"),
            ("1980-01-01", "2000-12-31", "%b %d, %Y", r"[A-Za-z]{3} \d{2}, \d{4}"),
            ("1980-01-01", "2000-12-31", "%d %b %Y", r"\d{2} [A-Za-z]{3} \d{4}"),
            ("1980-01-01", "2000-12-31", "%d %B %Y", r"\d{2} [A-Za-z]+ \d{4}"),
            ("1980-01-01", "2000-12-31", "%Y/%m/%d", r"\d{4}/\d{2}/\d{2}"),
            ("1980-01-01", "2000-12-31", "%Y.%m.%d", r"\d{4}\.\d{2}\.\d{2}"),
            ("1980-01-01", "2000-12-31", "%m/%d/%Y", r"\d{2}/\d{2}/\d{4}"),
            ("1980-01-01", "2000-12-31", "%m.%d.%Y", r"\d{2}\.\d{2}\.\d{4}"),
        ]
    )
    def test_generate_random_dob(
        self, start_date, end_date, date_format, regex_pattern
    ):
        generated_dob = generate_random_dob(start_date, end_date, date_format)

        # Check if the generated date matches the expected regex pattern
        date_pattern = re.compile(regex_pattern)
        self.assertTrue(
            re.match(date_pattern, generated_dob),
            f"Generated date {generated_dob} does not match the pattern {regex_pattern}",
        )

        # Additional check to ensure the date is within the specified range
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        generated_dt = datetime.strptime(generated_dob, date_format)

        self.assertGreaterEqual(
            generated_dt,
            start_dt,
            f"Generated date {generated_dob} is before start date {start_date}",
        )
        self.assertLessEqual(
            generated_dt,
            end_dt,
            f"Generated date {generated_dob} is after end date {end_date}",
        )


if __name__ == "__main__":
    unittest.main()
