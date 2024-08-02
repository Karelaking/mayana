from json import load
from typing import List
from pathlib import Path

from utils.loader import Loader

# Constants
ROOT = Path(__file__).parent.parent.parent
NAME_PATH = Path.joinpath(ROOT, "constants/states.json")
loader: Loader = Loader()


# load data
def load_data(path: str):
    try:
        with open(path, "r") as file:
            return load(file)
    except:
        raise FileNotFoundError


# generates random states
def states(country: str = "India", count: int = 1) -> str | List[str]: ...
