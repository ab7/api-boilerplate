# API Boilerplate

Starter code for quickly getting up and running on API development using the latest technologies. Underlying tech will change periodically based on best practices and improved options.

## What's included at a glance

* **Framework** - FastAPI
* **Database** - PostgreSQL
* **ORM** - SQLAlchemy
* **Database Migrations** - Alembic
* **Formatting** - autopep8
* **Tests** - pytest

## Docker Setup

* Make sure Docker for desktop is running. See [Docker Desktop](https://docs.docker.com/desktop/).
* Run the following command to build and start the containers in detached mode:

        docker-compose up -d --build

* Stop the containers:

        docker-compose down

* Stop the containers and remove volumes:

        docker-compose down -v

## Logging

* To view api logs:

        docker-compose logs -f api

* To view the database logs:

        docker-compose logs -f database

## Linting

* To run the linter use the following command:

        docker-compose run --rm api poetry run flake8 .

## Auto-formatting

* To automatically format the application code using the flake8 config run the following command:

        docker-compose run --rm api poetry run autopep8 -v --in-place --aggressive app/*.py

## Database setup

**Note:** If you changed the database username, password or database name in `db_init.env` you will also need to update them in `docker-compose.yml` and `alembic.ini`.

* Create migrations for current models:

        docker-compose run --rm api poetry run alembic revision --autogenerate -m "Create users table"

* Apply the migrations:

        docker-compose run --rm api poetry run alembic upgrade head

You can interact with the database via the command line or GUI. See [TablePlus](https://tableplus.com/) for a decent GUI.

## Running the example starter code

* Fire up your favorite API tool. The following commands use [httpie](https://httpie.org/).
* Create a user:

        http POST http://localhost:8000/users username=admin email=admin@admin.com

* Get users:

        http http://localhost:8000/users