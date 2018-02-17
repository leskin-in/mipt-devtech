FROM python:latest

ADD ./requirements.txt requirements.txt
ADD ./reader.py reader.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["reader.py", ""]
