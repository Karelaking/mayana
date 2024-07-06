from string import digits
from random import shuffle
from secrets import choice
from typing import List


def random_phone(count: int = 1, code: str = "+91", _format: str = '') -> str | List[str]:
    """
    Generates the random phone numbers.

    :param count: No. of output phone numbers
    :param code: Country code
    :param _format: Country specific format
    :return: returns the single or list of phone numbers
    """
    choices: List[str] = list(digits)
    print(choices)
    shuffle(choices)
    print(choices)

    if count != 1:
        phone: List[str] = []
        try:
            for _ in range(count):
                shuffle(choices)
                phone.append(code + ' ' + ''.join(choice(choices) for _ in range(10)))
        except:
            raise IndexError('')
        return phone
    else:
        try:
            shuffle(choices)
            return code + ' ' + ''.join(choice(choices) for _ in range(10))
        except:
            raise IndexError('')
