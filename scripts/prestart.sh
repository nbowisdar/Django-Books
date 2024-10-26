#! /usr/bin/env bash

set -e
set -x

# Let the DB start
# python app/backend_pre_start.py

# Run migrations
uv run manage.py migrate

uv run manage.py create_default_superuser

