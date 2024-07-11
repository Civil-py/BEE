services:
  - type: web
    name: your-service-name
    env: python
    buildCommand: |
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
    startCommand: gunicorn p.p.wsgi:application
