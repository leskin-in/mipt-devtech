#!/usr/bin/env bash

# Docker does not allow to connect to host machine. Linking is considered deprecated. => Do not dockerize the sender
# docker build -t reader:ivan ./reader/ > /dev/null
# docker run -t --network container:rabbitrecv reader:ivan

pip3 install pika > /dev/null
python3 reader/reader.py

