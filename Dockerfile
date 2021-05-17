# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /code/

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY . /code
COPY ./scripts/wait-for-it/wait-for-it.sh /code/wait-for-it.sh
RUN set -ex && pipenv install --deploy --system
RUN chmod u+x /code/wait-for-it.sh

CMD [\
    "gunicorn",\
    "app.server:application",\
    "-w", "2",\
    "--threads", "2",\
    "--access-logfile=-",\
    "-b", "0.0.0.0:5000"\
]