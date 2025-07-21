"""Logger module for rites package.

This module contains logging functionality including automatic log file creation,
formatting, and log management.
"""

from .logger import Logger, get_logger, get_sec_logger

__all__ = ['Logger', 'get_logger', 'get_sec_logger']
