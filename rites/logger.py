from datetime import datetime
from rituals import Misc
from enum import Enum
import atexit
import sys
import traceback

# TODO: Implement Log Levels
class LogLevels(Enum):
    """ LogLevels Enum

        Enum for log levels
    """
    INFO = 1
    DEBUG = 2
    WARNING = 3
    ERROR = 4
    SUCCESS = 5


class Logger:
    """ Logger Class

        Automatic log file creation and formatting

        Args:
            log_path (str): The path to the log file directory
            log_format (str): The format of the log file name - default (log-%Y-%m-%d-%Hh-%Mm-%Ss)
            log_inline_format (str): The format for the time stamp on the log lines - default ([%Y-%m-%d %H:%M:%S])
    """
    def __init__(self, log_path, log_format="log-%Y-%m-%d-%Hh-%Mm-%Ss", log_inline_format="[%Y-%m-%d %H:%M:%S]"):
        self.log_path = log_path
        self.log_format = log_format
        self.log_inline_format = log_inline_format
        self.logger_creation_time = self._getFormattedTimeStamp()

        atexit.register(self._exit_handler)

    def _getFormattedTimeStamp(self):
        now = datetime.now()
        return now.strftime(self.log_format)

    def _getInlineFormattedTimeStamp(self):
        now = datetime.now()
        return now.strftime(self.log_inline_format)

    def _writeToLogFile(self, txt):
        try:
            with open(f"{self.log_path}/{self.logger_creation_time}.log", "a+") as log_file:
                log_file.write(txt)
                log_file.close()
        except FileNotFoundError:
            open(f"{self.log_path}/{self.logger_creation_time}.log", "w").write(txt)

    def _exit_handler(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if exc_type is None:
            self.success("Program exited successfully.")
        else:
            self.error("Program exited with an error.")
            self.error("".join(traceback.format_exception(exc_type, exc_value, exc_traceback)))

    def warning(self, *txt):
        """ Logs a warning message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{Misc.ConsoleColors.white}[{Misc.ConsoleColors.rst}{Misc.ConsoleColors.warning}warning{Misc.ConsoleColors.rst}{Misc.ConsoleColors.white}]{Misc.ConsoleColors.rst} " + string)
        self._writeToLogFile(f"{self._getInlineFormattedTimeStamp()} [warning] {string}\n")

    def error(self, *txt):
        """ Logs an error message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{Misc.ConsoleColors.white}[{Misc.ConsoleColors.rst}{Misc.ConsoleColors.error}error{Misc.ConsoleColors.rst}{Misc.ConsoleColors.white}]{Misc.ConsoleColors.rst} " + string)
        self._writeToLogFile(f"{self._getInlineFormattedTimeStamp()} [error] {string}\n")

    def debug(self, *txt):
        """ Logs a debug message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{Misc.ConsoleColors.white}[{Misc.ConsoleColors.rst}{Misc.ConsoleColors.debug}debug{Misc.ConsoleColors.rst}{Misc.ConsoleColors.white}]{Misc.ConsoleColors.rst} " + string)
        self._writeToLogFile(f"{self._getInlineFormattedTimeStamp()} [debug] {string}\n")

    def success(self, *txt):
        """ Logs a success message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{Misc.ConsoleColors.white}[{Misc.ConsoleColors.rst}{Misc.ConsoleColors.success}success{Misc.ConsoleColors.rst}{Misc.ConsoleColors.white}]{Misc.ConsoleColors.rst} " + string)
        self._writeToLogFile(f"{self._getInlineFormattedTimeStamp()} [success] {string}\n")

    def info(self, *txt):
        """ Logs a success message

            Args:
                txt (str): The message to log
        """
        string = ""
        for substr in txt:
            string += str(substr) + " "
        print(f"{Misc.ConsoleColors.white}[{Misc.ConsoleColors.rst}{Misc.ConsoleColors.info}info{Misc.ConsoleColors.rst}{Misc.ConsoleColors.white}]{Misc.ConsoleColors.rst} " + string)
        self._writeToLogFile(f"{self._getInlineFormattedTimeStamp()} [info] {string}\n")

