Technical task is [here](https://docs.google.com/document/d/172UuYu7XkMgFWl_vEeYoIm9kKgR6Kfz3xUhd_ye5nBY/edit?tab=t.0) 


# Books Project

Welcome to the Books project! This Django application is designed to manage a collection of books and includes features for RESTful API endpoints, testing, and development utilities.

## Features

- **Auto-generated Documentation**: Automatically generate documentation for Django REST Framework using **drf-spectacular**.
- **Next Generation Python Manager**: Leverage **uv** for running Django management commands efficiently.
- **Simplified Management**: Utilize a **Makefile** to streamline common tasks and commands.
- **pgAdmin Web App**: Includes a web interface for managing PostgreSQL databases with pgAdmin.


## Project Settings

- **Django Application Name**: `books`
- **Django Management Command**: `uv run manage.py`

## Dependencies
### Uv
I'm using the nex gen package and project manager for python [Uv](https://github.com/astral-sh/uv)
To be able to run app without docker I need to install the UV.
```bash
pip install uv
```
### Django dependencies:

- **Core Dependencies**:
  - `django`: The web framework for building the application.
  - `django-filter`: A package for filtering querysets.
  - `djangorestframework`: Toolkit for building Web APIs.
  - `drf-spectacular`: For generating OpenAPI 3 schemas.
  - `psycopg2-binary`: PostgreSQL adapter for Python.
  - `python-dotenv`: For loading environment variables from `.env` files.

- **Development Dependencies**:
  - `faker`: A library for generating fake data.
  - `pytest`: A testing framework.
  - `pytest-django`: A plugin for integrating pytest with Django.

## Makefile Commands

This project includes a Makefile for easier management of common tasks. Here are the available commands:

### Available Commands:

- `make run-dev`: Run the development server.
- `make migrate`: Apply database migrations locally for SQLite.
- `make makemigrations`: Create new migrations based on model changes.
- `make shell`: Open the Django shell.
- `make test`: Run the project tests.

### Docker Commands:
- `make run-watch`: Run the development server inside a Docker container with file watching enabled.
- `make run-prod`: Run the production server using Docker.
- `make stop`: Stop the Docker containers.
- `make test-postgres`: Run tests in a Docker container with PostgreSQL.

## Getting Started

1. **Clone the Repository**:
```bash
git clone https://github.com/nbowisdar/Django-Books
cd Django-Books
```

* Without Docker:
    ```bash
    # Install uv
    pip install uv
    
    # Apply migrations
    make migrate

    # Start server
    make run-dev
    ```

* With Docker:
    ```bash
    make run-watch - For dev only.
    make run-prod - For prod.
    ```

## Testing
It's also 2 way of testing.

1. With Postgres and with Docker
    ```bash
    make test-postgres
    ```

2. With SQLite and without Docker
    ```bash
    make test
    ```
3. Also this is possible to generate dummy books for testing purposes. 
    ```bash
    uv run manage.py generate_books
    ``` 
Note.

I haven't configured a full production setup with Nginx, Traefik, Gunicorn, and separate settings to keep the focus on Django REST Framework rather than on DevOps concerns."

This version clarifies your intent and improves the flow of the sentence. Let me know if you’d like any further adjustments!