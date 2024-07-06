from random import choice
from typing import List

# Sample lists of first names and last names
FIRST_NAME = [
    "John",
    "Jane",
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Edward",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Jack",
    "Katherine",
    "Liam",
    "Mia",
    "Noah",
    "Olivia",
    "Paul",
    "Quincy",
    "Rachel",
    "Samuel",
    "Tina",
    "Uma",
    "Victor",
    "Wendy",
    "Xander",
    "Yara",
    "Zachary",
]

LAST_NAME = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "King",
]


def random_name(count:int = 1) -> str | List[str]:
    """
    Generates the random names

    :param count: No. of output names
    :return: returns the single of list of names
    """

    if count == 1:
        return f"{choice(FIRST_NAME)} {choice(LAST_NAME)}"
    else:
        return [f"{choice(FIRST_NAME)} {choice(LAST_NAME)}" for _ in range(count)]
