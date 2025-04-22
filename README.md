# Requirements

## Installation

    pip install -r ./requirements.txt

## Freeze

    pip freeze > requirements.txt

## Enviroments

    MYSQL_HOST=
    MYSQL_PORT=
    MYSQL_DB=
    MYSQL_USER=
    MYSQL_PASSWORD=

## Run the app

    uvicorn app.main:app --reload

## Ruff Format code

    ruff format .
    
## Ruff check linting

    ruff check .

## Before pushing to github

- ruff check .
- ruff format .
- pyright
- pytest -v

## Preview migration

    alembic upgrade head --sql




