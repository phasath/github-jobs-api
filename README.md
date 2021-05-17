# Jobs4You API

This is a simple implementation of an interface to the github jobs api. Our plan here is to:

1 - Use Python as our language for the backend, PyEnv to manage the Python Version (3.9) and PipEnv not only to manage the packages but also to allow us making use of Pipfile.
2 - Use vanilla javascript, css and html to do the necessary front-end part. I intend to create a very simple front-end.
3 - I am not quite sure whether I should collect the jobs asyncronously to feed the database in order to optimize the queries. As it is not clear to me when reading the description, I will proceed with the simplest solution as this is expected to be done within a week. If I were to do this, I would either use another language for this, like NodeJS or GO, to fill the database in another repository, or use celery with async tasks here. 
4 - As a way to improve the queries, I'll make use of Redis to cache the results, however, I will set a very short TTL as I suppose that there are new jobs and jobs getting filled in a high frequency. 
5 - I will make use of Connexion and OpenAPI to create a documentation for the API and to check the input and our API response.
6 - I will use Docker to set up the application, the database and the redis instance.
7 - I will deploy this application to heroku. 

# How to run

## Dependencies

This repository depends on the usage of:
- [Docker](https://docs.docker.com/engine/install/) 
- [Docker-Compose](https://docs.docker.com/compose/install/)

If you want to run locally, you will also need:
- [PipEnv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

## Building

To build the project, use:
```shell
$ docker-compose up
```

## Start

To start the project, use:
```shell
$ docker-compose start
```

If you want to run locally but make use of the database only, you can run:

```shell
$ docker-compose start postgres migrations
```
With the database started, you can use the `pipenv`:

```shell
$ pipenv install
$ pipenv shell
$ pipenv run local
```

Note that `local` is a script inside `Pipfile` that starts a local development server to make usage of auto-reloading and debugging.

## Tests

To run the tests, you can use:

```shell
$ pipenv install
$ pipenv shell
$ pipenv run tests
```

# PipEnv Autohooks

This repository is making use of Pipenv autohooks to auto-format the code using black. 

This is installed running:
```shell
$ pipenv run autohooks activate
```