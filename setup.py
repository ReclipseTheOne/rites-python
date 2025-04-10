import os
import rites.rituals
from dotenv import load_dotenv
from setuptools import setup, find_packages

p = rites.rituals.Misc

load_dotenv(".env")
pkgVersion = os.getenv('RITES_PKG_VERSION')
p.print_info(f"Building package with version {pkgVersion}")

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