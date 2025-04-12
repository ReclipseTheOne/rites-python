from colored import Fore, Style


class Printer:
    class __Style:
        def __init__(self, word: str, r: int, g: int, b: int):
            if len(word) != 3:
                raise ValueError("Style word is not 3 letters")
            if not (0 <= r <= 255):
                raise ValueError("Red value is not in [0, 255]")
            if not (0 <= g <= 255):
                raise ValueError("Green value is not in [0, 255]")
            if not (0 <= b <= 255):
                raise ValueError("Blue value is not in [0, 255]")

            self._word = word
            self._style = Fore.RGB(r, g, b)

        @property
        def word(self) -> str:
            return self._word

        @property
        def style(self) -> str:
            return self._style

        @word.setter
        def set_word(self, word: str):
            if len(word) != 3:
                raise ValueError("Style word is not 3 letters")
            self._word = word

        @style.setter
        def set_style(self, r: int, g: int, b: int):
            if 0 <= r <= 255:
                raise ValueError("Red value is not in [0, 255]")
            if 0 <= g <= 255:
                raise ValueError("Green value is not in [0, 255]")
            if 0 <= b <= 255:
                raise ValueError("Blue value is not in [0, 255]")
            self._style = Fore.RGB(r, g, b)

        def get_str(self) -> str:
            return f"{Fore.white}[{Style.reset}{self.style}{self.word}{Style.reset}{Fore.white}]{Style.reset}"

        def get_simple_string(self) -> str:
            return f"[{self.word}]"

    def __init__(self):
        self.Colors: dict = {
            "gray": Fore.RGB(100, 100, 100)
        }

        self.Styles: dict = {
            "debug": Printer.__Style("DBG", 128, 128, 128),
            "success": Printer.__Style("SCS", 20, 255, 20),
            "error": Printer.__Style("ERR", 255, 0, 0),
            "warning": Printer.__Style("WRN", 255, 255, 0),
            "info": Printer.__Style("INF", 0, 240, 255)
        }

    def get_style(self, key: str) -> __Style:
        return self.Styles[key]

    def get_color(self, key: str) -> str:
        return self.Colors[key]

    def add_style(self, key: str, word: str, r: int, g: int, b: int):
        """Add a custom style to the Printer Object

        Args:
            key (str): The name of the style
            word (str): The 3 letter word that will be displayed
            r (int): Red Value
            g (int): Green Value
            b (int): Blue Value
        """
        self.Styles[key] = Printer.__Style(word, r, g, b)

    def print_warning(self, *txt):
        """ Prints a warning message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style("warning").get_str()} {Fore.white}{string}{Style.reset}")

    def print_error(self, *txt):
        """ Prints an error message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style("error").get_str()} {Fore.white}{string}{Style.reset}")

    def print_debug(self, *txt):
        """ Prints a debug message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style("debug").get_str()} {Fore.white}{string}{Style.reset}")

    def print_info(self, *txt):
        """ Prints an info message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style("info").get_str()} {Fore.white}{string}{Style.reset}")

    def print_success(self, *txt):
        """ Prints a success message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style("success").get_str()} {Fore.white}{string}{Style.reset}")

    def print_custom(self, style_key: str, *txt):
        """ Prints a message using the Style specified

            Args:
                style_key (str): The style to be used (eg. success)
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.get_style(style_key).get_str()} {Fore.white}{string}{Style.reset}")
