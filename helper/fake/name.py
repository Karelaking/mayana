from json import load
from typing import List
from secrets import choice
import re

# Constants
NAME_PATH: str = "../../constants/name.json"


# Sample data for different countries
def load_data(path=NAME_PATH) -> dict:
    try:
        with open(path, "r") as file:
            return load(file)
    except:
        raise FileNotFoundError


# Generates random names
def generate_name(country: str, is_middle_name: bool) -> str:
    first_name = choice(names_data[country]["first_names"])
    last_name = choice(names_data[country]["last_names"])

    if is_middle_name:
        middle_name = choice(names_data[country]["middle_names"])

        full_name: str = f"{first_name} {middle_name} {last_name}"
        # Ensure the name follows a specific pattern
        if not re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+){1,2}$", full_name):
            raise ValueError(
                f"Generated name '{full_name}' does not match the required pattern"
            )
        return full_name
    else:

        full_name: str = f"{first_name} {last_name}"
        # Ensure the name follows a specific pattern
        if not re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+){1,2}$", full_name):
            raise ValueError(
                f"Generated name '{full_name}' does not match the required pattern"
            )
        return full_name


names_data = load_data()


def name(
    country: str = "India", count: int = 1, is_middle_name=False
) -> str | List[str]:
    """
    Generates the random names

    :param count: No. of output names
    :param is_middel_name: Add middel names
    :return: returns the single of list of names
    """

    if country not in names_data:
        raise ValueError(
            f"Country '{country}' not supported. Available countries: {', '.join(names_data.keys())}"
        )

    if count != 1:
        names: List[str] = []
        for _ in range(count):
            names.append(generate_name(country=country, is_middle_name=is_middle_name))
        return names

    else:
        return generate_name(country=country, is_middle_name=is_middle_name)


if __name__ == "__main__":
    print(name())
