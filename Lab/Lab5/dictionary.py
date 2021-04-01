from file_handler import FileHandler


class Dictionary:
    def __init__(self):
        self.__dictionary = None

    def load_dictionary(self, file_path):
        self.__dictionary = FileHandler.load_data(file_path)

    def query_definition(self, word):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
