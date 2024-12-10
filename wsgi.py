# wsgi.py
# run with this gunicorn --workers 5 --bind 0.0.0.0:5000 wsgi:app
from main import app

if __name__ == "__main__":
    app.run()
