import re
import random
from typing import List, Union


def generate_random_ip(format: str = "IPv4") -> str:
    """
    Generate a random IP address of the specified format.

    Parameters:
    format (str): The format of the IP address to generate. Supported formats are 'IPv4' and 'IPv6'.
                  Defaults to 'IPv4'.

    Returns:
    str: A randomly generated IP address.

    Raises:
    ValueError: If the generated IP does not match the expected format or if an unsupported format is specified.
    """
    if format == "IPv4":
        # Generate an IPv4 address
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

        # Validate using regex
        ip_pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
        if not ip_pattern.match(ip):
            raise ValueError("Generated IP does not match the expected IPv4 format.")

        return ip

    elif format == "IPv6":
        # Generate an IPv6 address
        ip = ":".join("{:x}".format(random.randint(0, 65535)) for _ in range(8))

        # Validate using regex
        ip_pattern = re.compile(r"^([\da-f]{1,4}:){7}[\da-f]{1,4}$")
        if not ip_pattern.match(ip):
            raise ValueError("Generated IP does not match the expected IPv6 format.")

        return ip

    else:
        raise ValueError("Unsupported IP format. Use 'IPv4' or 'IPv6'.")


def ip(format: str = "IPv4", count: int = 1) -> Union[str, List[str]]:
    """
    Generate one or more random IP addresses of the specified format.

    Paramets:
    format (str): The format of the IP address to generate. Supported formats are 'IPv4' and 'IPv6'.
                  Defaults to 'IPv4'.
    count (int): The number of IP addresses to generate. Defaults to 1.

    Returns:
    Union[str, List[str]]: A single IP address if count is 1, or a list of IP addresses if count is greater than 1.
    """
    if count != 1:
        return [generate_random_ip(format=format) for _ in range(count)]
    else:
        return generate_random_ip(format=format)

