import sys
from setuptools import setup, find_packages

pkgVersion = "INVALID_VERSION"

# Default version from file
with open("rites/_version.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            pkgVersion = line.split("=")[1].strip().replace('"', '').replace("'", '')
            break

# Check for version argument
for arg in sys.argv:
    if arg.startswith('--version='):
        pkgVersion = arg.split('=')[1]
        # Remove this argument so setuptools doesn't see it
        sys.argv.remove(arg)
        break

print(f"Building package with version {pkgVersion}")

setup(
    name="rites",
    version=pkgVersion,
    description="Reclipse's Initial Try at Enhanced Simplicity or R.I.T.E.S. A simple and lightweight QoL module.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Reclipse",
    maintainer="Reclipse",
    url="https://github.com/ReclipseTheOne/rites",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'colored>=2.2.4'
    ]
)
