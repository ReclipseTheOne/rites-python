import time
import math

from rites import rites

r = rites.Rites()
class Chrono:
    def __init__(self):
        self.__init_time = time.time_ns()
        self.__stopwatch_tabs = []

    def stopwatch(self, print=True):
        if print:
            r.print_debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        self.__stopwatch_tabs.append(str(time.time_ns()))

    def get_stopwatch_tabs(self):
        return self.__stopwatch_tabs