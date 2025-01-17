FROM python:3.12

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /app

WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "FlaskServer:app", "-b :8000"]