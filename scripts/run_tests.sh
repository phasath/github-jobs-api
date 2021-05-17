#!/usr/bin/env bash
set -o errexit -o nounset -o pipefail

export ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[ -z "${REVISION_TAG:-}" ] && export GIT_REVISION=$(git rev-parse --short HEAD) || export GIT_REVISION=${REVISION_TAG}

export FLASK_APP=app.server
export FLASK_ENV=development
export FLASK_DEBUG=True

set +e
docker rm jobs4you_test &>/dev/null
docker stop postgres-test &>/dev/null
docker rm postgres-test &>/dev/null
set -e

docker build \
    --target "jobs4you_test" \
    -t "test/jobs4you:${GIT_REVISION}" \
    "${ROOT}"

docker run -d \
    --name "postgres-test" \
    --env "POSTGRES_PASSWORD=postgres" \
    postgres:13-alpine

if [ $# -eq 0 ]; then
    docker run -ti \
        -v "${ROOT}":/code \
        --name "jobs4you_test" \
        --link "postgres-test:postgres-test" \
        --env "PGPASSWORD=postgres" \
        --env "PGDATABASE=postgres" \
        --env "PGHOST=postgres-test" \
        "test/jobs4you:${GIT_REVISION}" \
        "scripts/pytest.sh"
else
    docker run -ti \
        -v "${ROOT}":/code \
        --name "jobs4you_test" \
        --link "postgres-test:postgres-test" \
        --env "PGPASSWORD=postgres" \
        --env "PGDATABASE=postgres" \
        --env "PGHOST=postgres-test" \
        "test/jobs4you:${GIT_REVISION}" \
        "${@:-}"
fi
