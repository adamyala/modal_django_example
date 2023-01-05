# Modal django example

## Installation and local server

```shell
# activate your python virtual environment
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment

```shell
# activate your python virtual environment

# create environment variables
# you only have to create secrets once per project
# get a db url before this step. i like elephantsql.com for free hobby dbs
modal secret create demo-secrets DATABASE_URL=<database url> SECRET_KEY=<a long random string>
# collect static files locally to be pushed
python manage.py collectstatic --no-input
# deploy web endpoint
modal deploy config/modal_wsgi.py
# deploy scheduled jobs
modal deploy config/modal_jobs.py
```

### Modal specific files

- `config/__init__.py` initializes secrets, image, and mounts used for modal
- `config/modal_settings.py` sets remote `SECRET_KEY` variable and connects to remote postgres database
- `config/modal_wsgi.py` wsgi entry point for web endpoint
- `config/modal_jobs.py` calls django command to run scheduled jobs





