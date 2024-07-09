# from typing import List
# from secrets import choice
# from random import shuffle
# from string import ascii_lowercase, ascii_uppercase, digits, punctuation


# def random_password(
#         count: int = 1,
#         length: int = 10,
#         is_lower_case: bool = True,
#         is_upper_case: bool = False,
#         is_digits: bool = False,
#         is_punctuation: bool = False,
# ) -> str | List[str]:
#     """
#     Generates the random password

#     :param count: No. of output passwords
#     :param length: Length of the single password
#     :param is_lower_case: Use lower case latter's
#     :param is_upper_case: Use upper case latter's
#     :param is_digits: Use digits
#     :param is_punctuation: User punctuations
#     :return: returns the single or list of passwords

#     rtype:
#     """

#     # creates a string to generate random password
#     LATTERS: str = ""
#     if is_digits:
#         LATTERS += digits
#     if is_upper_case:
#         LATTERS += ascii_uppercase
#     if is_lower_case:
#         LATTERS += ascii_lowercase
#     if is_punctuation:
#         LATTERS += punctuation

#     if count != 1:
#         password: List[str] = []

#         for _ in range(count):
#             shuffle(list(LATTERS))
#             try:
#                 password.append("".join(choice(LATTERS) for _ in range(length)))
#             except:
#                 raise IndexError("")
#         return password

#     else:
#         try:
#             shuffle(list(LATTERS))
#             return "".join(choice(LATTERS) for _ in range(length))
#         except:
#             raise IndexError("")


import random
import string
import re


def password(
    length=12,
    is_use_digits=False,
    is_use_lower_case=True,
    is_use_upper_case=False,
    is_use_punctuation=False,
):
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    # Create character pools based on parameters
    char_pools = []
    if is_use_digits:
        char_pools.append(string.digits)
    if is_use_lower_case:
        char_pools.append(string.ascii_lowercase)
    if is_use_upper_case:
        char_pools.append(string.ascii_uppercase)
    if is_use_punctuation:
        char_pools.append(string.punctuation)

    if not char_pools:
        raise ValueError("At least one character pool must be selected")

    # Concatenate all character pools into one string
    all_chars = "".join(char_pools)

    # Generate the password using random choices from the pool
    password = "".join(random.choice(all_chars) for _ in range(length))

    # Ensuring at least one character from each selected pool is in the password
    while True:
        password_valid = True
        if is_use_digits and not re.search(r"\d", password):
            password_valid = False
        if is_use_lower_case and not re.search(r"[a-z]", password):
            password_valid = False
        if is_use_upper_case and not re.search(r"[A-Z]", password):
            password_valid = False
        if is_use_punctuation and not re.search(
            r"[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]", password
        ):
            password_valid = False

        if password_valid:
            break
        else:
            password = "".join(random.choice(all_chars) for _ in range(length))

    return password

