@echo off
REM Ensure you have the necessary tools installed
pip install setuptools wheel twine

REM Build your package
python setup.py sdist bdist_wheel

REM Upload your package to PyPI
python -m twine upload dist/*