export FLASK_APP=app.server
export FLASK_ENV=development
export FLASK_DEBUG=True

if [ $# -eq 0 ]; then
    pytest --cov-report term-missing --cov=app tests
else
    pytest --cov-report term-missing --cov=app "${@:-}"
fi