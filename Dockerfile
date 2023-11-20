FROM python:3.12.0-bookworm

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
