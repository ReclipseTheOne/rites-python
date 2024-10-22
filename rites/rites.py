from colored import Fore, Style
from pathlib import Path


class Rites:
    """ Rites Class

        The main class for utility methods.
    """
    def __init__(self):
        self.__c_red = Fore.red
        self.__c_blue = Fore.blue
        self.__c_green = Fore.green
        self.__c_white = Fore.white
        self.__c_yellow = Fore.yellow
        self.__c_rst = Style.reset

    def print_warning(self, *txt):
        """ Prints a warning message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_yellow}warning{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_error(self, *txt):
        """ Prints an error message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_red}error{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_debug(self, *txt):
        """ Prints a debug message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_blue}debug{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_success(self, *txt):
        """ Prints a success message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_green}success{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def get_file_count(self, directory):
        """ Returns the number of files in a directory

            Args:
                directory (str): Absolute path to the directory
        """
        dir_path = Path(directory)
        file_count = len([file for file in dir_path.iterdir() if file.is_file()])

        return file_count

    def get_file_paths(self, directory):
        """ Returns a list of absolute paths to all the files in a directory

            Args:
                directory (str): Absolute path to the directory
        """
        paths = []

        dir_path = Path(directory)
        for file in dir_path.iterdir():
            if file.is_file():
                paths.append(str(file.absolute().resolve()))

        return paths

    def enforce(self, obj, cls, debug=False):
        """ Enforces a type on an object

            Args:
                obj (object): The object to enforce the type on
                cls (type): The type to enforce
                debug (bool): Whether to print debug messages (default False)
        """
        if not isinstance(obj, cls):
            if debug:
                self.print_error(f"Blocked: {obj}")
            raise TypeError(f"Expected type: <{cls.__name__}> but got <{type(obj).__name__}>")
        if debug:
            self.print_success(f"Passed: {obj}")
