export FLASK_APP=app.server:application
export FLASK_ENV=development
export FLASK_DEBUG=True
export PGHOST=localhost
export IS_LOCAL=True

flask run -h 0.0.0.0 -p 5000
