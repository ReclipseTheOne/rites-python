from datetime import datetime
from colored import Fore, Style


class Logger:
    """ Logger Class

        Automatic log file creation and formatting

        Args:
            log_path (str): The path to the log file directory
            log_format (str): The format of the log file name - default (log-%Y-%m-%d-%Hh-%Mm-%Ss)
    """
    def __init__(self, log_path, log_format="log-%Y-%m-%d-%Hh-%Mm-%Ss"):
        self.log_path = log_path
        self.log_format = log_format
        self.__c_red = Fore.red
        self.__c_blue = Fore.blue
        self.__c_green = Fore.green
        self.__c_white = Fore.white
        self.__c_yellow = Fore.yellow
        self.__c_rst = Style.reset

    def _getLogDateTime(self):
        now = datetime.now()
        return now.strftime(self.log_format)

    def _writeToLogFile(self, txt):
        try:
            with open(f"{self.log_path}/{self._getLogDateTime()}", "a+") as log_file:
                log_file.write(txt)
                log_file.close()
        except FileNotFoundError:
            open(f"{self.log_path}/{self._getLogDateTime()}", "w").write(txt)

    def warning(self, *txt):
        """ Logs a warning message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.__c_white}[{self.__c_rst}{self.__c_yellow}warning{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)
        self._writeToLogFile(f"[warning] {string}\n")

    def error(self, *txt):
        """ Logs an error message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.__c_white}[{self.__c_rst}{self.__c_red}error{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)
        self._writeToLogFile(f"[error] {string}\n")

    def debug(self, *txt):
        """ Logs a debug message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.__c_white}[{self.__c_rst}{self.__c_blue}debug{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)
        self._writeToLogFile(f"[debug] {string}\n")

    def success(self, *txt):
        """ Logs a success message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{self.__c_white}[{self.__c_rst}{self.__c_green}success{self.__c_rst}{self.__c_white}]{self.__c_rst} " + string)
        self._writeToLogFile(f"[success] {string}\n")
