# Imports
from secrets import choice
from random import shuffle
import string
from typing import List
import re


# Generate the password using random choices from the pool
def generate_random_password(
    char_pool: str,
    length: int,
    is_digits: bool,
    is_lower: bool,
    is_upper: bool,
    is_punctuation: bool,
):
    shuffle(list(char_pool))
    password = "".join(choice(char_pool) for _ in range(length))

    # Ensuring at least one character from each selected pool is in the password
    while True:
        password_valid = True
        if is_digits and not re.search(r"\d", password):
            password_valid = False
        if is_lower and not re.search(r"[a-z]", password):
            password_valid = False
        if is_upper and not re.search(r"[A-Z]", password):
            password_valid = False
        if is_punctuation and not re.search(
            r"[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]", password
        ):
            password_valid = False

        if password_valid:
            return password
        else:
            generate_random_password(
                char_pool=char_pool,
                is_digits=is_digits,
                is_lower=is_lower,
                is_upper=is_upper,
                is_punctuation=is_punctuation,
                length=length,
            )


def password(
    length=12,
    count: int = 1,
    is_digits=False,
    is_lower=True,
    is_upper=False,
    is_punctuation=False,
) -> str | List[str]:
    """
    Generates the random password

    :param count: No. of output passwords
    :param length: Length of the single password
    :param is_lower: Use lower case latter's
    :param is_upper: Use upper case latter's
    :param is_digits: Use digits
    :param is_punctuation: User punctuations
    :return: returns the single or list of passwords

    rtype:
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    # Create character pools based on parameters
    char_pools = []
    if is_digits:
        char_pools.append(string.digits)
    if is_lower:
        char_pools.append(string.ascii_lowercase)
    if is_upper:
        char_pools.append(string.ascii_uppercase)
    if is_punctuation:
        char_pools.append(string.punctuation)

    if not char_pools:
        raise ValueError("At least one character pool must be selected")

    # Concatenate all character pools into one string
    char_pool = "".join(char_pools)

    if count != 1:
        return [
            generate_random_password(
                char_pool=char_pool,
                is_digits=is_digits,
                is_lower=is_lower,
                is_upper=is_upper,
                is_punctuation=is_punctuation,
                length=length,
            ) 
            for _ in range(count)
        ]

    else:
        return generate_random_password(
            char_pool=char_pool,
            is_digits=is_digits,
            is_lower=is_lower,
            is_upper=is_upper,
            is_punctuation=is_punctuation,
            length=length,
        )
