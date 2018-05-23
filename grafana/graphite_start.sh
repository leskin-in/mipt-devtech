#!/usr/bin/env bash

sudo docker run -d \
--name graphite \
--rm \
-v /var/graphite/conf:/opt/graphite/conf \
-v /var/graphite/data:/opt/graphite/storage \
-v /var/graphite/statsd:/opt/statsd \
-p 80:80 \
-p 2003-2004:2003-2004 \
-p 2023-2024:2023-2024 \
-p 8125:8125/udp \
-p 8126:8126 \
graphiteapp/graphite-statsd
