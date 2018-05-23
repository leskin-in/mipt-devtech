#!/usr/bin/env bash

sort $1 | awk -f reducer.awk
