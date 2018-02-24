#!/usr/bin/env bash

docker rmi itodo592:latest
docker build -t itodo592:latest .
docker run --name itodo592 -p 127.0.0.1:80:8000 -d --rm itodo592

