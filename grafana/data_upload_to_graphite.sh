#!/usr/bin/env bash

while read p; do
	echo $p | nc localhost 2003
done <$1

