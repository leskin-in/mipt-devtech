#!/usr/bin/env bash

cd storage                                                                                                                                  
docker-compose build > /dev/null
docker-compose up

