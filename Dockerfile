FROM python:3.9-slim-buster as base

# Perform common operations, dependency installation etc...
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN pip install poetry 
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY . /app
#ENV POETRY_HOME=/poetry
#ENV PATH=${POETRY_HOME}/bin:${PATH}
EXPOSE 5000
FROM base as production
ENTRYPOINT ["poetry", "run", "gunicorn", "--config", "gunicorn_config.py", "todo_app.app:create_app()"]


FROM base as development
# Configure for local development
ENV FLASK_ENV=development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]

FROM base as test
# Configure for local development
ENV FLASK_ENV=development


RUN apt-get update -qqy && apt-get install -qqy wget gnupg unzip
# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
&& apt-get update -qqy \
&& apt-get -qqy install google-chrome-stable \
&& rm /etc/apt/sources.list.d/google-chrome.list \
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*
# Install Chrome WebDriver
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
&& CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
&& echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
&& wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
&& unzip /tmp/chromedriver_linux64.zip -d /usr/bin \
&& rm /tmp/chromedriver_linux64.zip \
&& chmod 755 /usr/bin/chromedriver
ENTRYPOINT ["poetry", "run", "pytest"]




