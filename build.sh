# build and check the project's release artifacts

# preconditions
[ -z "$VIRTUAL_ENV" ] && echo "Run $(basename "$0") within a virtual environment" && exit 1
cd -- "$(dirname -- "$(readlink -f -- "$0")")" || exit 1

set -xe

# build dist/mypak-0.0.1.tar.gz
python -m build

# build dist/mypak-0.0.1-py3-none-any.whl and do not build wheels for dependencies (sick defaults)
pip wheel . -w dist --no-deps
