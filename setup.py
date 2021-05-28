import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), './version.py')) as f:
    exec(f.read().strip())  # pylint: disable=exec-used

install_requires = [
    'autopep8==1.5.*',
    'autoflake==1.4',
    'click==7.1.*',
    'isort==5.7.*',
    'docformatter==1.4',
    'unify==0.5'
]

setup(
    name='pyformat',
    author='Orestis Zambounis',
    author_email='me@orestisz.com',
    version=version,  # pylint: disable=undefined-variable
    py_modules=['pyformat'],
    install_requires=install_requires,
    entry_points={'console_scripts': ['pyformat=pyformat:auto_format']}
)
