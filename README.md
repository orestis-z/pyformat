# Python Formatter

`pyformat` is a simple CLI tool to format your Python code.

The libary is based on [autopep8](https://pypi.org/project/autopep8/), [autoflake](https://pypi.org/project/autoflake/), [isort](https://pypi.org/project/isort/), [docformatter](https://pypi.org/project/docformatter/), and [unify](https://pypi.org/project/unify/):

* Formats code to follow the PEP 8 style guide (using [autopep8](https://pypi.org/project/autopep8/)).
* Removes unused imports (using [autoflake](https://pypi.org/project/autoflake/)).
* Sort and group imports (using [isort](https://pypi.org/project/isort/)).
* Formats docstrings to follow PEP 257 (using [docformatter](https://pypi.org/project/docformatter/)).
* Makes strings all use the same type of quote where possible (using [unify](https://pypi.org/project/unify/)).

## Installation

```
pip install git+ssh://git@github.com/orestis-z/pyformat.git
```

## Usage

Recursive:

```
pyformat -r
```

Selected file:

```
pyformat hello_world.py
```

## Development

```
pip install -e .
```

## Todo

* Use native python packages for autopep8, autoflake, etc. instead of calling `os.system(...)`
* Add plugins for editors
