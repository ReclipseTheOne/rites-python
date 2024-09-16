from setuptools import setup, find_packages

setup(
    name="rites",
    version="0.1.0",
    description="Reclipse's Initial Try at Enhanced Simplicity or R.I.T.E.S. A simple and lightweight QoL module.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Reclipse",
    url="https://github.com/ReclipseTheOne/rites",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)