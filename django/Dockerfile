FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django
ADD . /django/

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install Django

ENTRYPOINT ["python3", "/django/manage.py", "runserver", "0.0.0.0:8000"]

