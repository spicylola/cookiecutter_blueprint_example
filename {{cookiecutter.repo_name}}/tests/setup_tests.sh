#!/usr/bin/env bash
set -eo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
pushd $SCRIPT_DIR

# Create a Test Db with a Postgres Instance, refer to docker-compose.yml
docker-compose up -d

echo 'Waiting for PGSQL to start'
until pg_isready -h ${DB_HOST:-localhost} -p ${DB_PORT-5432} 2>&1 > /dev/null
do
    echo -n '.'
done
echo ''
echo 'Initializing Test DB'
popd
