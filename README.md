# FastAdmin

FastAdmin is a fullstack skeleton project for build admin dashboard wil most features and strong tools based on FastAPI & VueJS.

## Features

- [ ] Authentication & Authorization.
- [ ] Role Base Access Controller (RBAC).
- [ ] Background Job with Celery.
- [ ] Build-in Mailable (Auth mails, ..etc).
- [ ] Event handler.
- [ ] Database Schemas, Models, Migration & Seeding.
- [ ] Tesing for feature & unit.
- [ ] Build-in Coder Generator, CURD, Scaffolding module.

## Preview

**Screenshot**

!["FastAdmin Dashboard"](screenshot.png)

## Quickstart

**Setup environment**

```shell
# Create python virtual environment
virtualenv -p python3.7 venv-py3.7
source venv-py3.7/bin/activate
pip install -r requirements.in

# Run FastAdmin
uvicorn App.main:app --reload --port 8009
```

## Development


Create a new model and migrations

```shell
cd App

# Create new model
orator make:model Post -m

# Create migration
orator make:migration create_users_table --table=users
orator make:migration add_softdeletes_to_users_table --table=users


# run migrate
orator migrate -c Database/db.py

# rollbacke migration
orator migrate:rollback -c Database/db.py

# Refresh
orator migrate:refresh --seed -c Database/db.py
```

Seeding fake data

```shell
export PYTHONPATH="<project_path>/FastAdmin"
orator db:seed --seeder users_table_seeder -c Database/db.py
```
