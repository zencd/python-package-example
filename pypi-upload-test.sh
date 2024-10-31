# preconditions
[ -z "$VIRTUAL_ENV" ] && echo "Run $(basename "$0") within a virtual environment" && exit 1
cd -- "$(dirname -- "$(readlink -f -- "$0")")" || exit 1

set -x
twine upload -r testpypi dist/mypak-*.whl
