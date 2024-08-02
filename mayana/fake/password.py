from secrets import choice
from random import shuffle
import string
from typing import List, Union
import re
import typer


def generate_random_password(
    char_pool: str,
    length: int,
    is_digits: bool,
    is_lower: bool,
    is_upper: bool,
    is_punctuation: bool
) -> str:
    """
    Generates a random password using characters from the specified character pool.

    This function ensures the generated password contains at least one character
    from each selected character type (digits, lowercase, uppercase, punctuation).

    Args:
        char_pool (str): Pool of characters to choose from.
        length (int): Desired length of the password.
        is_digits (bool): Whether to include digits in the password.
        is_lower (bool): Whether to include lowercase letters in the password.
        is_upper (bool): Whether to include uppercase letters in the password.
        is_punctuation (bool): Whether to include punctuation characters in the password.

    Returns:
        str: Generated password.
    """
    char_pool_list = list(char_pool)
    shuffle(char_pool_list)
    password = "".join(choice(char_pool_list) for _ in range(length))

    # Ensure at least one character from each selected pool is included in the password
    while True:
        password_valid = True
        if is_digits and not re.search(r"\d", password):
            password_valid = False
        if is_lower and not re.search(r"[a-z]", password):
            password_valid = False
        if is_upper and not re.search(r"[A-Z]", password):
            password_valid = False
        if is_punctuation and not re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]", password):
            password_valid = False

        if password_valid:
            return password
        else:
            password = "".join(choice(char_pool_list) for _ in range(length))


def password(
    length: int = typer.Option(12, prompt=True),
    count: int = typer.Option(1, prompt=True),
    is_digits: bool = typer.Option(False, prompt=True),
    is_lower: bool = typer.Option(False, prompt=True),
    is_upper: bool = typer.Option(False, prompt=True),
    is_punctuation: bool = typer.Option(False, prompt=True)
) -> Union[str, List[str]]:
    """
    Generates one or more random passwords based on specified criteria.

    This function allows customization of password length and the inclusion
    of specific character types such as digits, lowercase letters, uppercase letters,
    and punctuation characters.

    Args:
        length (int, optional): Length of the password(s). Must be greater than 0. Defaults to 12.
        count (int, optional): Number of passwords to generate. Defaults to 1.
        is_digits (bool, optional): Include digits in the password(s). Defaults to False.
        is_lower (bool, optional): Include lowercase letters in the password(s). Defaults to True.
        is_upper (bool, optional): Include uppercase letters in the password(s). Defaults to False.
        is_punctuation (bool, optional): Include punctuation characters in the password(s). Defaults to False.

    Returns:
        Union[str, List[str]]: A single password if count is 1, otherwise a list of passwords.

    Raises:
        ValueError: If the password length is less than or equal to 0.
        ValueError: If no character pools are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

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

    char_pool = "".join(char_pools)

    if count > 1:
        return [
            generate_random_password(
                char_pool=char_pool,
                length=length,
                is_digits=is_digits,
                is_lower=is_lower,
                is_upper=is_upper,
                is_punctuation=is_punctuation
            )
            for _ in range(count)
        ]
    else:
        return generate_random_password(
            char_pool=char_pool,
            length=length,
            is_digits=is_digits,
            is_lower=is_lower,
            is_upper=is_upper,
            is_punctuation=is_punctuation
        )


# typer.run(password)
