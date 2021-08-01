FROM python:3.9-slim-buster as base
# Perform common operations, dependency installation etc...
RUN apt-get update; apt-get install curl -y
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN pip install poetry 
WORKDIR /app
COPY . /app
#ENV POETRY_HOME=/poetry
#ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN poetry install
EXPOSE 5000
FROM base as production
ENTRYPOINT ["poetry", "run", "gunicorn", "--config", "gunicorn_config.py", "todo_app.app:create_app()"]


FROM base as development
# Configure for local development
ENV FLASK_ENV=development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]




