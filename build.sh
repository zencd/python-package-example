set -xe
# build dist/mypak-0.0.1.tar.gz
python setup.py sdist
# build dist/mypak-0.0.1-py3-none-any.whl
python setup.py bdist_wheel
twine check dist/*
