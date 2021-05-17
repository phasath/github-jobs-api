#!/usr/bin/env bash
set -o errexit -o nounset -o pipefail

export ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

pytest --cov-report html:test-reports/coverage --cov-report term-missing --cov=app tests
