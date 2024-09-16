import colored
import sys
import os

from _version import __version__

def version():
    """Version number for rites.

    Returns:
      str: package version number
    """
    return __version__

def about():
    """Prints the installed version numbers for rites and its dependencies,
    and some system info.

    Please include this information in bug reports.
    """

    print(
        "Rites is a simple and lightweight QoL module\n",
        "An ever growing tool box\n"
    )

    print("Colored Version:            {}".format(colored.__version__))
    print("Rites Version:              {}".format(__version__))
    print("Python Version:             {}".format(*sys.version_info[0:3]))
    print("Installation Path:          {}".format(os.path.dirname(__file__)))