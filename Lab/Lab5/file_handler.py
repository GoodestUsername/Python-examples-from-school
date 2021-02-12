from enum import Enum
from pathlib import Path
import json


class FileExtensions(Enum):
    TXT = ".txt"
    JSON = ".json"

    @classmethod
    def is_valid_extension(cls, file_extension):
        return file_extension in cls._value2member_map_


class FileHandler:
    @staticmethod
    def load_data(path, file_extension):
        if not Path(path).exists():
            raise FileNotFoundError

        if FileExtensions.is_valid_extension(file_extension):
            with open(path, mode='r', encoding='utf-8') as data_file:
                if file_extension is FileExtensions.JSON.value:
                    return json.load(data_file)
                else:
                    return data_file.read()

        else:
            raise InvalidFileTypeError("File type is not supported exception")

    @staticmethod
    def write_lines(path, lines):
        if not Path(path).exists():
            raise FileNotFoundError

        with open(path, mode='a', encoding='utf-8') as data_file:
            data_file.write(lines)


class InvalidFileTypeError(Exception):
    def __init__(self, my_msg):
        super().__init__(my_msg)
