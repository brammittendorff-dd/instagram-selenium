#!/bin/bash
# wait-for-selenium.sh

set -e

url="$1"
shift
cmd="$@"

until wget -O- "$url"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd