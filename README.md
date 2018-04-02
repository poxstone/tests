# Simple tests cases
Simpes test caeses for python

## Install 
    pip install --upgrade pep8
    pip install --upgrade pyflakes

## PEP8 test strings
    python -m pycodestyle ./strings-py/test.py
    python -m pyflakes ./strings-py/test.py

## Unit tests
    python -m unittest discover -s ./strings-py/ -p *.py
    python -m unittest discover -s ./widgets-py/ -p *.py
    # or
    cd strings; python -m unittest test

