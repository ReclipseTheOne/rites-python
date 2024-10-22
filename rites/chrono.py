import time
import math

from rites import rites, logger
r = rites.Rites()


class Chrono:
    """ Chrono Class

        Has methods for timing and stopwatching code execution

        Args - AS OF 0.1.3:
            logger (logger.Logger): Your logger object - default (None)
    """
    def __init__(self, logger: logger.Logger = None):
        self.__init_time = time.time_ns()
        self.__stopwatch_tabs = []
        self.logger = logger

    def stopwatch(self, print=True):
        """ Tabs the current time on method call

        Keyword arguments:
            print: bool -- (default True)
        """
        if print and self.logger:
            self.logger.debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        elif print and not self.logger:
            r.print_debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        self.__stopwatch_tabs.append(str(time.time_ns()))

    def get_stopwatch_tabs(self):
        # Returns all the saved stopwatch tabs
        return list(self.__stopwatch_tabs)

    def reset_stopwatch_tabs(self):
        self.__stopwatch_tabs = []
