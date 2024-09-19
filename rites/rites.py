from colored import Fore, Style
from pathlib import Path


class Rites:
    def __init__(self):
        self.__c_red = Fore.red
        self.__c_blue = Fore.blue
        self.__c_green = Fore.green
        self.__c_white = Fore.white
        self.__c_yellow = Fore.yellow
        self.__c_rst = Style.reset

    def print_warning(self, *txt):
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_yellow}warning{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_error(self, *txt):
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_red}error{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_debug(self, *txt):
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_blue}debug{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def print_success(self, *txt):
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(
            f"{self.__c_white}[{self.__c_rst}{self.__c_green}success{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)

    def get_file_count(self, directory):

        dir_path = Path(directory)
        file_count = len([file for file in dir_path.iterdir() if file.is_file()])

        return file_count

    def get_file_paths(self, directory):
        paths = []

        dir_path = Path(directory)
        for file in dir_path.iterdir():
            if file.is_file():
                paths.append(str(file.absolute().resolve()))

        return paths

    def enforce(self, obj, cls, debug=False):
        if not isinstance(obj, cls):
            if debug:
                self.print_error(f"Blocked: {obj}")
            raise TypeError(f"Expected type: <{cls.__name__}> but got <{type(obj).__name__}>")
        if debug:
            self.print_success(f"Passed: {obj}")