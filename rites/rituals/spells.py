from pathlib import Path
from printer import Printer
from colored import Fore, Style


class Spells:
    '''
        Random functions that I use on a regular basis
    '''

    p = Printer()

    @staticmethod
    def get_file_count(directory: str) -> int:
        """ Returns the number of files in a directory

            Args:
                directory (str): Absolute path to the directory
        """
        dir_path = Path(directory)
        file_count = len([file for file in dir_path.iterdir() if file.is_file()])

        return file_count

    @staticmethod
    def get_file_paths(directory: str) -> list:
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

    @staticmethod
    def enforce(obj, cls, debug=True):
        """ Enforces a type on an object

            Args:
                obj (object): The object to enforce the type on
                cls (type): The type to enforce
                debug (bool): Whether to print debug messages (default True)
        """
        if not isinstance(obj, cls):
            if debug:
                Spells.p.print_error(f"{Fore.white}Blocked: {obj}{Style.white}")
                Spells.p.print_error(f"Expected type: {Fore.white}<{Style.rst}{Fore.red}{cls.__name__}{Style.rst}{Fore.white}>{Style.rst} but got {Fore.white}<{Style.rst}{Fore.red}{type(obj).__name__}{Style.rst}{Fore.white}>{Style.rst}")
            raise TypeError(f"Expected type: <{cls.__name__}> but got <{type(obj).__name__}>")
