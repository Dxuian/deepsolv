#!/bin/bash

# Apply database migrations
python insta/manage.py makemigrations
python insta/manage.py migrate

# Start the server
exec "$@"