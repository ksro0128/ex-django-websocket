python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
