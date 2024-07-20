import re
from json import load
from pathlib import Path
from secrets import choice
from typing import List, Union

# Constants
ROOT = Path(__file__).parent.parent.parent
NAME_PATH: str = str(Path.joinpath(ROOT, "constants/name.json"))


# Sample data for different countries
def load_data(path=NAME_PATH) -> dict:
    """
    Load name data from a JSON file.

    Parameters:
    path (str): The path to the JSON file containing the name data. Defaults to NAME_PATH.

    Returns:
    dict: A dictionary containing the name data.

    Raises:
    FileNotFoundError: If the specified file cannot be found.
    """
    try:
        with open(path, "r") as file:
            return load(file)
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")


# Generates random names
def generate_name(country: str, is_middle_name: bool) -> str:
    """
    Generate a random name based on the specified country and middle name preference.

    Parameters:
    country (str): The country for which to generate the name.
    is_middle_name (bool): Whether to include a middle name in the generated name.

    Returns:
    str: A randomly generated name.

    Raises:
    ValueError: If the generated name does not match the required pattern.
    """
    first_name = choice(names_data[country]["first_names"])
    last_name = choice(names_data[country]["last_names"])

    if is_middle_name:
        middle_name = choice(names_data[country]["middle_names"])
        full_name: str = f"{first_name} {middle_name} {last_name}"
    else:
        full_name: str = f"{first_name} {last_name}"

    # Ensure the name follows a specific pattern
    if not re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+){1,2}$", full_name):
        raise ValueError(
            f"Generated name '{full_name}' does not match the required pattern"
        )

    return full_name


names_data = load_data()


# @click.command()
# @click.option('--country', prompt="Enter country name", default="India", help=("he country for which to generate the "
#                                                                                "name(s). Defaults to "
#                                                                                "'India'"))
def name(
        country: str = "India", count: int = 1, is_middle_name: bool = False
) -> Union[str, List[str]]:
    """
    Generate one or more random names based on the specified country and middle name preference.

    Parameters:
    country (str): The country for which to generate the name(s). Defaults to "India".
    count (int): The number of names to generate. Defaults to 1.
    is_middle_name (bool): Whether to include a middle name in the generated name(s). Defaults to False.

    Returns:
    Union[str, List[str]]: A single name if count is 1, or a list of names if count is greater than 1.

    Raises:
    ValueError: If the specified country is not supported.
    """
    if country not in names_data:
        raise ValueError(
            f"Country '{country}' not supported. Available countries: {', '.join(names_data.keys())}"
        )

    if count != 1:
        names: List[str] = [
            generate_name(country=country, is_middle_name=is_middle_name)
            for _ in range(count)
        ]
        return names
    else:
        return generate_name(country=country, is_middle_name=is_middle_name)
