# How to develop a Python package

A reliable file structure and workflow for purposes of Python 3 package development.

## File structure

    project-root
    ├── src
    │   └── mypak
    │       ├── __init__.py
    │       └── sub.py
    ├── test
    │   └── test_1.py
    ├── prepare-dev.sh
    └── test.sh

## Development workflow

Once:
- create and activate a venv
- run `prepare-dev.sh`

Iteratively:
- change anything in `src/mypak/*.py`
- run tests: `test.sh`

A new dependency added into `setup.py`:
- rerun `prepare-dev.sh`

## What you get

- Smooth development process;
- all symbols are resolved in IDE;
- you can run tests clicking in IDE;
- you can run tests in terminal;
- you can do it from any directory;
- no need to hack `PYTHONPATH` or `sys.path`;
- no need in special IDE support;
- changes in your package are automatically visible in tests;
- no need in relative imports, such as `import ..src.mypak`;
- do `import mypak`, just like clients will do;
- no excessive `__init__.py` needed;
- tests won't appear in release artifacts;
- all requirements are defined in a single place: `setup.py`;
- PyCharm CE successfully auto-detects any changes there;
- no deprecated things used, as of 2024.

## Test

    pytest test/

## Build

    ./build.sh

Now expect artifacts like `dist/mypak-0.0.1-py3-none-any.whl`
and `dist/mypak-0.0.1.tar.gz` to appear.

## Install

Inside another project/venv, you can install package `mypak` in any of the following ways, but `whl` and PyPi are faster:

```bash
(venv)
pip install dist/mypak-0.0.1-py3-none-any.whl
pip install dist/mypak-0.0.1.tar.gz
pip install /path/to/python-package-example
pip install https://github.com/zencd/python-package-example/archive/master.zip
pip install mypack  # from PyPi, if you uploaded it
python -c 'import mypak'  # verify
```
