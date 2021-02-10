from enum import Enum


class FileExtensions(Enum):
    TXT = ".txt"
    JSON = ".json"


class FileHandler:
    @staticmethod
    def load_data(path, file_extension):
        pass

    @staticmethod
    def write_lines(path, lines):
        pass


class InvalidFileTypeClass(Exception):
    def __init__(self, my_msg):
        super().__init__(my_msg)
