web: bin/start-nginx gunicorn -c config/gunicorn.conf.py --bind=unix:/tmp/gunicorn.sock secret_sharing.wsgi:app --log-file -
