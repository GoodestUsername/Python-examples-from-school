"""
Modules contains interface and concrete methods for (EN/DE)cryption handlers.
"""
import abc
import des
import enum
from pathlib import Path


class ValidKeyLengths(enum.Enum):
    """
    Enum of valid key lengths.
    """
    eight = 8
    sixteen = 16
    twenty_four = 24

    @classmethod
    def has_value(cls, value):
        """
        return boolean of if value is in enum.

        :source: https://stackoverflow.com/questions/43634618/how-do-i-test-if-int-value-exists-in-python-enum
        -without-using-try-catch :param value: a number :return: a boolean
        """
        return value in cls._value2member_map_

    @classmethod
    def __str__(cls):
        """
        Return string representation of the enum.
        :return: a String.
        """
        str_value = ""
        for value in cls._value2member_map_:
            str_value += value + ", "

        return str_value[:-2]


class CryptionHandler(abc.ABC):
    """
    Baseclass for all handlers that handle (en/de)cryption.
    Each handler can maintain a reference to another handler
    thereby enabling the chain of responsibility pattern.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request):
        """
        Each handlers specific handling method.
        :param request: the request to (en/de)crypt.
        :return: The (en/de) crypted result.
        """
        pass

    def set_handler(self, handler):
        """
        Sets the next handler in the chain.
        :param handler: a CryptionHandler
        """
        self.next_handler = handler

    @staticmethod
    def get_start_of_encryption_chain():
        # handler setup
        validate_key_handler = IsValidKeyHandler()
        validate_file_handler = InputFileHandler()
        encryption_handler = EncryptionHandler()
        post_encryption_handler = PostCryptionHandler()
        file_output_handler = FileOutputHandler()

        # set handler order, validate_key_handler > validate_file_handler > encryption_handler > post_encryption_handler
        validate_key_handler.next_handler(validate_file_handler)
        validate_file_handler.next_handler(encryption_handler)
        encryption_handler.set_handler(post_encryption_handler)
        post_encryption_handler.set_handler(file_output_handler)

        return validate_key_handler

    @staticmethod
    def get_start_of_decryption_chain():
        # handler setup
        validate_key_handler = IsValidKeyHandler()
        validate_file_handler = InputFileHandler()
        decryption_handler = DecryptionHandler()
        post_encryption_handler = PostCryptionHandler()
        file_output_handler = FileOutputHandler()

        # set handler order, validate_key_handler > validate_file_handler > decryption_handler > post_encryption_handler
        validate_key_handler.next_handler(validate_file_handler)
        validate_file_handler.next_handler(decryption_handler)
        decryption_handler.set_handler(post_encryption_handler)
        post_encryption_handler.set_handler(file_output_handler)

        return validate_key_handler


class IsValidKeyHandler(CryptionHandler):
    """
    Handles validating the key.
    """

    def handle_request(self, request):
        if ValidKeyLengths.has_value(len(request.data_input)):
            self.next_handler.handle_request(request)
        else:
            raise KeyLengthNotValidError("Key length is not valid, need to be one of :" + ValidKeyLengths.__str__)


class InputFileHandler(CryptionHandler):
    """
    Handles file to read from, sets data input to file content, raises FileNotFoundError if the file doesnt exist.
    """

    def handle_request(self, request):
        """
        Handles file from request.
        :param request: a Request.
        """
        path = request.input_file
        if path is not None:
            if not Path(path).exists():
                raise FileNotFoundError
            else:
                with open(path, mode='rb') as data:
                    request.data_input = data.read()

        self.next_handler.handle_request(request)


class PostCryptionHandler(CryptionHandler):
    """
    Handles request after result has been determined.
    """
    def handle_request(self, request):
        """
        Handles request after result has been calculated.
        :param request: a Request
        """
        if request.output == "print":
            print(request.result)
        else:
            self.next_handler.handle_request(request)


class FileOutputHandler(CryptionHandler):
    """
    Handles writing result to file.
    """
    def handle_request(self, request):
        """
        Write result to file.
        :param request: a Request
        """
        with open(request.output, mode='wb') as data:
            data.write(request.result)


class EncryptionHandler(CryptionHandler):
    """
    Handles the encryption
    """

    def handle_request(self, request):
        """
        Handles decryption from request.
        :param request: a Request.
        """
        request.result = des.DesKey(request.key).encrypt(request.data_input)

        self.next_handler.handle_request(request)


class DecryptionHandler(CryptionHandler):
    """
    Handles the decryption
    """

    def handle_request(self, request):
        """
        Handles decryption from request.
        :param request: a Request.
        """
        request.result = des.DesKey(request.key).decrypt(request.data_input)

        self.next_handler.handle_request(request)


class KeyLengthNotValidError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
