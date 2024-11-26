import time
import math
import logger
import rituals

misc = rituals.Misc

class Chrono:
    """ Chrono Class

        Has methods for timing and stopwatching code execution
        Methods:
            stopwatch: Tabs the current time on method call
            get_stopwatch_tabs: Returns all saved stopwatch tabs
            reset_stopwatch_tabs: Resets all saved stopwatch tabs

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
            misc.print_debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        self.__init_time = time.time_ns()
        self.__stopwatch_tabs.append(str(time.time_ns()))

    def get_stopwatch_tabs(self):
        # Returns all the saved stopwatch tabs
        return list(self.__stopwatch_tabs)

    def reset_stopwatch_tabs(self):
        self.__stopwatch_tabs = []
