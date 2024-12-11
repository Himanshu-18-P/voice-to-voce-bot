# wsgi.py
# run with this gunicorn --workers 4 --bind 0.0.0.0:port wsgi:app , #  https://haier.interactivedemos.io/
from main import app

if __name__ == "__main__":
    app.run()
