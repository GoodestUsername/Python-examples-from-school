from Lab.Lab3.libraryitem import LibraryItem


class Journal(LibraryItem):
    """
    Represents a single journal in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, issue_number, publisher):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param issue_number: a string
        :param publisher: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._issue_number = issue_number
        self._publisher = publisher
        super().__init__(call_num, title, num_copies)

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"