# preconditions
cd -- "$(dirname -- "$(readlink -f -- "$0")")" || exit 1

set -x
rm -rf */__pycache__ build/ dist/ src/*.egg-info
