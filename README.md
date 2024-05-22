python -m venv venv \n
source venv/bin/activate \n
pip install -r requirements.txt \n
gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 \n
