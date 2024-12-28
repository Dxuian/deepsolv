#!/bin/bash

/code/wait-for-it.sh db:3306 --timeout=30 --strict -- echo "MySQL is up - starting web service"

exec "$@"
