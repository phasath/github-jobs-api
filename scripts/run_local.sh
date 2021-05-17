export FLASK_APP=app.server:application
export FLASK_ENV=development 
export FLASK_DEBUG=True 
export PGHOST=localhost

flask run -h 0.0.0.0 -p 5000