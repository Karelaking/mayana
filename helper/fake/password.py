from typing import List
from secrets import choice
from random import shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def random_password(
        count: int = 1,
        length: int = 10,
        is_lower_case: bool = True,
        is_upper_case: bool = False,
        is_digits: bool = False,
        is_punctuation: bool = False,
) -> str | List[str]:
    """
    Generates the random password

    :param count: No. of output passwords
    :param length: Length of the single password
    :param is_lower_case: Use lower case latter's
    :param is_upper_case: Use upper case latter's
    :param is_digits: Use digits
    :param is_punctuation: User punctuations
    :return: returns the single or list of passwords

    rtype:
    """

    # creates a string to generate random password
    LATTERS: str = ""
    if is_digits:
        LATTERS += digits
    if is_upper_case:
        LATTERS += ascii_uppercase
    if is_lower_case:
        LATTERS += ascii_lowercase
    if is_punctuation:
        LATTERS += punctuation

    if count != 1:
        password: List[str] = []

        for _ in range(count):
            shuffle(list(LATTERS))
            try:
                password.append("".join(choice(LATTERS) for _ in range(length)))
            except:
                raise IndexError("")
        return password

    else:
        try:
            shuffle(list(LATTERS))
            return "".join(choice(LATTERS) for _ in range(length))
        except:
            raise IndexError("")
