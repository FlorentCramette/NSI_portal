#!/bin/bash
set -e

echo "Running database migrations..."
python manage.py migrate --noinput || {
    echo "Migration failed! Exiting..."
    exit 1
}

echo "Creating staticfiles..."
python manage.py collectstatic --noinput --clear || echo "Collectstatic failed, continuing..."

echo "Starting Gunicorn on port ${PORT:-8000}..."
exec gunicorn nsi_project.wsgi:application \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
