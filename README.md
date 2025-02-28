## Simple FastAPI Cookiecutter Template with FastAPI users

Will create FastAPI app with fastapi-users integrated with predefined apps structure pre-commit.

## Project Structure

```shell
├── REAMDE.md
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── logic.py
│   │   └── schemas.py
│   ├── main.py
│   ├── settings.py
│   └── test_app
│       ├── __init__.py
│       └── views.py
├── pyproject.toml
├── test_app.db
```

You have `auth` ready to use with [fastapi-users](https://github.com/fastapi-users/fastapi-users) integrated
And test application `test_app` with just one route `/welcome` in order to check the token

## Predefined packages

Template uses `pip-tools` with the following `requirements.in`

```shell
fastapi[standard]
sqlalchemy
fastapi-users
fastapi-users-db-sqlalchemy
fastapi-users
uvicorn
pre-commit
aiosqlite
```

## Database

For now its simple sqlite
And credentials are stored in `.env` file

```shell
DATABASE_URL=sqlite+aiosqlite:///./test_app.db
```

## Quick start

```shell
cookiecutter https://github.com/lexluter1988/cookiecutter-fastapi-users.git

pip install pip-tools
make deps
```

## Starting the app

```shell script
uvicorn --host 0.0.0.0 --port 5000 --reload app.main:application
```
