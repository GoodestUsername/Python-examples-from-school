from Lab.Lab3.book import Book
from Lab.Lab3.dvd import DVD
from Lab.Lab3.journal import Journal


class LibraryItemGenerator(object):
    @staticmethod
    def generate_library_item():
        item_type = get_item_type_from_user()
        library_item_attributes = get_library_item_attributes_from_user()
        return build_library_item(item_type, library_item_attributes)


def get_item_type_from_user():
    user_input = None
    while user_input not in range(1, 4):
        print("\nAdd an item to the library.")
        print("-----------------------")
        print("1. Add a Book")
        print("2. Add a DVD")
        print("3. Add a Journal")

        string_input = input("Please enter your choice (1-3)")

        if string_input == '':
            continue

        user_input = int(string_input)
    return user_input


def get_library_item_attributes_from_user():
    call_number = input("Enter Call Number: ")

    title = input("Enter title: ")

    num_copies = int(input("Enter number of copies "
                           "(positive number): "))

    return call_number, title, num_copies


def build_library_item(item_type, library_item_attributes):
    if item_type == 1:
        return build_book(library_item_attributes)

    elif item_type == 2:
        return build_dvd(library_item_attributes)

    elif item_type == 3:
        return build_journal(library_item_attributes)


def build_book(library_item_attributes):
    author = input("Enter author name")

    return Book(library_item_attributes[0], library_item_attributes[1], library_item_attributes[2], author)


def build_dvd(library_item_attributes):
    release_date = input("Enter release_date")
    region_code = input("Enter region_code")

    return DVD(library_item_attributes[0], library_item_attributes[1], library_item_attributes[2],
               release_date, region_code)


def build_journal(library_item_attributes):
    names = input("Enter names")
    issue_number = input("Enter issue_number")
    publisher = input("Enter publisher")

    return Journal(library_item_attributes[0], library_item_attributes[1], library_item_attributes[2],
                   names, issue_number, publisher)
