FROM python:3.12.0-bookworm

WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
