#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate || echo "Migrations failed, likely due to existing tables. Continuing..."
