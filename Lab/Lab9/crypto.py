import argparse
import enum

from cryptionhandler import CryptionHandler, KeyLengthNotValidError


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)  # key. need to check if en or de, or neither
        request.data_input = args.string  # -s, no need to check
        request.input_file = args.file  # -f, inputted file, need to check if file exists
        request.output = args.output  # -o, output to file, need to check if directory exists
        request.key = args.key  # key, need to check length
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:
    """
    Class to handle en/decryption Requests.
    """
    def __init__(self):
        """
        Constructor, sets up the start of handlers.
        """
        self.encryption_start_handler = CryptionHandler.get_start_of_encryption_chain()

        self.decryption_start_handler = CryptionHandler.get_start_of_decryption_chain()

    def execute_request(self, request: Request):
        """
        Executes the (en/de)cryption request.
        :param request: a Request.
        """
        if request.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.handle_request(request)

        elif request.encryption_state == CryptoMode.DE:
            self.encryption_start_handler.handle_request(request)

        else:
            print("Mode does not exist")


def main(request: Request):
    crypto = Crypto()
    try:
        crypto.execute_request(request)
    except FileNotFoundError:
        print("The file to (en/de) crypt does not exist.")

    except KeyLengthNotValidError as caught_error:
        print(caught_error)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
