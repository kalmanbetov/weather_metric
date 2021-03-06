#!/bin/sh

set -e

case "$1" in
    start)
        echo "Running App (gunicorn)..."
        exec gunicorn --reload -b 0.0.0.0:${BACKEND_WEB_PORT:-4} -w ${BACKEND_API_WEB_CONCURRENCY:-4} core.wsgi:application
    ;;
    migrate)
        echo "Running migrate to DB..."
        exec python manage.py migrate
    ;;
    *)
        exec $@
    ;;
esac
