# python-skeleton

This repository contains a skeleton setup for a Python project. As such the idea is that a clone of this repo can serve as the starting point for the development of a Python package.

---

## pyenv

The suggested dependency manager is pyenv. Given the pipfile within the repo, you can instantiate a virtual environment with:

`pipenv install`

to build the environment and then

`pipenv shell`

to activate the environment. Exit with `deactivate`.

Use `pipenv lock` to update environment with new (versions of) dependencies. 

## Build and publish package with PyPI

Make sure you have the latest update of build

`python3 -m pip install --upgrade build`

Build package

`python3 -m build`

Update twine

`python3 -m pip install --upgrade twine`

Upload to PyPI

`twine upload dist/* `
