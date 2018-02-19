FROM python:latest

ADD . /storage

WORKDIR /storage

EXPOSE 5672

RUN pip install --upgrade pip
RUN pip install pika pymongo

ENTRYPOINT ["python3", "receiver.py"]

