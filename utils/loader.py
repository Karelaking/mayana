import os.path
from pickle import load, dump
from pathlib import Path
import json


class Loader:
    def __init__(self):
        self.__ROOT: Path = Path(os.path.normpath(os.path.dirname(__file__))).parent.parent

    @staticmethod
    def load_data(file_path: Path) -> dict:
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
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found.")

    @staticmethod
    def dump_data(file_path: Path, data: dict):
        try:
            with open(file_path, 'rb') as file:
                dump(data, file)
        except FileNotFoundError:
            raise FileNotFoundError

    @staticmethod
    def pickler_decoder(file_path: Path) -> dict:
        try:
            with open(file_path, 'rb') as file:
                data = load(file)
                return data
        except FileNotFoundError:
            raise FileNotFoundError

    def pickler_encoder(self, data: dict, file_name: Path):
        with open(f'{self.root}/constants/{file_name}', 'wb') as file:
            dump(data, file)
