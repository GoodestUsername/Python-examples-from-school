from Lab.Lab3.libraryitem import LibraryItem


class DVD(LibraryItem):
    """
    Represents a single journal in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._release_date = release_date
        self._region_code = region_code
        super().__init__(call_num, title, num_copies)

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release date: {self._release_date}\n" \
               f"Region code: {self._region_code}"
