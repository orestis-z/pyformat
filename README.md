# Python Formatter

`pyformat` is a simple CLI tool to format your Python code.

The libary is based on [autopep8](https://pypi.org/project/autopep8/), [autoflake](https://pypi.org/project/autoflake/), [isort](https://pypi.org/project/isort/), [docformatter](https://pypi.org/project/docformatter/), and [unify](https://pypi.org/project/unify/).

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
