FROM python:latest

ADD . /reader

WORKDIR /reader

RUN pip install --upgrade pip
RUN pip install pika

ENTRYPOINT ["python3", "reader.py"]

