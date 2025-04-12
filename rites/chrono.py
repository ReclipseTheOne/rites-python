from .logger import Logger
from .rituals.printer import Printer

import time
import math
import functools


class Chrono:
    """Chrono Class

       Contains time and timing functions for your heart's content
    """

    def __init__(self, logger: Logger = None):
        self.__init_time = time.time_ns()
        self.__stopwatch_tabs = []
        self.__printer = Printer()
        self.__function_timings = {}
        self.logger = logger

    def stopwatch(self, print=True):
        """ Tabs the current time on method call

        Keyword arguments:
            print: bool -- (default True)
        """
        if print and self.logger:
            self.logger.debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        elif print and not self.logger:
            self.__p.print_debug(f"Time since last stopwatch: {math.floor((time.time_ns() - self.__init_time) / 1000000) / 1000}s")
        self.__init_time = time.time_ns()
        self.__stopwatch_tabs.append(str(time.time_ns()))

    def get_stopwatch_tabs(self):
        # Returns all the saved stopwatch tabs
        return list(self.__stopwatch_tabs)

    def reset_stopwatch_tabs(self):
        self.__stopwatch_tabs = []

    def time_function(self, name=None):
        """ Decorator to time function execution in seconds

        Args:
            name (str, optional): Custom name for the timing entry. Defaults to function name.

        Returns:
            function: Decorated function that logs timing information
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()

                execution_time = end_time - start_time

                # Use provided name or function name
                func_name = name if name else func.__name__

                # Store timing information
                if func_name not in self.__function_timings:
                    self.__function_timings[func_name] = []
                self.__function_timings[func_name].append(execution_time)

                if self.logger:
                    self.logger.debug(f"Function '{func_name}' executed in {execution_time:.6f}s")
                else:
                    self.__printer.print_debug(f"Function '{func_name}' executed in {execution_time:.6f}s")

                return result
            return wrapper
        return decorator

    def time_function_ns(self, name=None):
        """ Decorator to time function execution in nanoseconds

        Args:
            name (str, optional): Custom name for the timing entry. Defaults to function name.

        Returns:
            function: Decorated function that logs timing information
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time_ns()
                result = func(*args, **kwargs)
                end_time = time.time_ns()

                # Calculate execution time in nanoseconds
                execution_time = end_time - start_time

                # Use provided name or function name
                func_name = name if name else func.__name__

                # Store timing information
                if func_name not in self.__function_timings:
                    self.__function_timings[func_name] = []
                self.__function_timings[func_name].append(execution_time)

                # Log timing info with appropriate formatting (ms for readability)
                formatted_time = f"{execution_time / 1_000_000:.6f}ms"
                if self.logger:
                    self.logger.debug(f"Function '{func_name}' executed in {formatted_time}")
                else:
                    self.__printer.print_debug(f"Function '{func_name}' executed in {formatted_time}")

                return result
            return wrapper
        return decorator

    def get_function_timings(self, func_name=None):
        """ Get timing statistics for a specific function or all functions

        Args:
            func_name (str, optional): The function name to get timings for. 
                                      If None, returns all timings. Defaults to None.

        Returns:
            dict: Dictionary containing timing statistics
        """
        if func_name and func_name in self.__function_timings:
            timings = self.__function_timings[func_name]
            return {
                'name': func_name,
                'count': len(timings),
                'total': sum(timings),
                'average': sum(timings) / len(timings) if timings else 0,
                'min': min(timings) if timings else 0,
                'max': max(timings) if timings else 0,
                'timings': timings
            }
        elif func_name:
            return {'error': f"No timings found for function '{func_name}'"}
        else:
            result = {}
            for name, timings in self.__function_timings.items():
                result[name] = {
                    'count': len(timings),
                    'total': sum(timings),
                    'average': sum(timings) / len(timings) if timings else 0,
                    'min': min(timings) if timings else 0,
                    'max': max(timings) if timings else 0
                }
            return result

    def reset_function_timings(self, func_name=None):
        """ Reset timing statistics for a specific function or all functions

        Args:
            func_name (str, optional): The function name to reset timings for. 
                                      If None, resets all timings. Defaults to None.
        """
        if func_name:
            if func_name in self.__function_timings:
                self.__function_timings[func_name] = []
        else:
            self.__function_timings = {}
