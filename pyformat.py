import os
from pathlib import Path

import click


@click.command(
    context_settings=dict(
        help_option_names=['-h', '--help'],
        allow_extra_args=True),
    short_help='Auto-format python files.')
@click.option('--recursive', '-r', is_flag=True,
              help='Format all files starting from current directory recursively')
@click.pass_context
def auto_format(ctx, recursive):
    files = ctx.args
    if recursive:
        if len(files) != 0:
            raise ValueError("Don't specify file(s) for the recursive option")
        files = '.'
        extra_flags = '--recursive'
    else:
        if len(files) == 0:
            raise ValueError(
                "Please specify the file(s) you want to format or use the '--recursive' flag")
        files = ' '.join(files)
        extra_flags = ''

    click.echo('Removing unused variables and imports [autoflake]')
    os.system(
        f'autoflake --in-place --remove-all-unused-imports --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables {extra_flags} {files}')

    click.echo('Formatting code [autopep8]')
    os.system(
        f'autopep8 --in-place --aggressive --aggressive {extra_flags} {files}')

    click.echo('Cleaning up imports [isort]')
    os.system(f'isort --lai 2 {files}')

    click.echo('Formatting strings [unify]')
    os.system(f'unify --in-place {extra_flags} {files}')

    click.echo('Formatting docstrings [docformatter]')
    os.system(f'docformatter --in-place {extra_flags} {files}')

    click.echo('Running basic sanitizer')
    paths = list(Path('.').rglob('*')) if recursive else files
    _strip_files(paths)


def _strip_files(paths):
    paths = list(Path('.').rglob('*'))
    for path in paths:
        if os.path.isdir(path):
            continue
        try:
            with open(path, 'r') as f:
                contents = f.read()
            with open(path, 'w') as f:
                new_contents = contents.strip()
                if new_contents:
                    new_contents += '\n'
                f.write(new_contents)
        except UnicodeDecodeError:
            pass
