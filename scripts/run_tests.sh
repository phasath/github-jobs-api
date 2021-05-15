export FLASK_APP=app.server
export FLASK_ENV=development
export FLASK_DEBUG=True

pytest --cov=app tests