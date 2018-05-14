# Mega uWSGI framework

This mega web framework allows you to visit main page of the app, and hello page where you can put in your name via 'name' param.

## Installation

In order to run the server you need to clone this repo, install uWSGi on you machine, and run it.

```bash
git clone https://github.com/samuraii/otus_python_uwsgi_task4
```

Then you have to make pip install
```bash
pip install -r requirements.txt
```

In order to install uwsgi follow the documentation: https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

To run the application:

```bash
uwsgi --http :9090 --wsgi-file index.py
```

## Usage

After your server is running open:
http://localhost:9090/hello?name=SuperUser

Tada...

## Project purpose

Educational.