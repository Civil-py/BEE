services:
  - type: web
    name: bee-web
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt && python p/manage.py collectstatic --noinput"
    startCommand: "gunicorn p.p.wsgi:application"
    staticPublishPath: static
