#!/usr/bin/env python3

import time
import datetime
import sys
from string import ascii_uppercase


with open(sys.argv[1], 'r') as f:
    strings = f.readlines()

    last_value_identifier = None
    ascii_n = -1
    first_line_read = False
    for s in strings:
        if not first_line_read:
            first_line_read = True
            continue
        values = s.split(",")

        # Remove quotes
        for i in range(len(values)):
            values[i] = values[i][1:-1]
        values[len(values) - 1] = values[len(values) - 1][:-1]

        # Process data
        if last_value_identifier != values[0]:
            last_value_identifier = values[0]
            ascii_n += 1
        values[0] = ascii_uppercase[ascii_n]
        values[1] = "2012-" + values[1]
        values[1] = str(int(time.mktime(datetime.datetime.strptime(values[1], "%Y-%m-%dT%H:%M:%S").timetuple())))

        # Output
        res = "weather" + values[0] + " " + values[2] + " " + values[1]
        print(res)

