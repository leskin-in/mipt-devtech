#!/usr/bin/env python3

import sys

from simpledis import SimpleDis


with open(sys.argv[1], "r") as f:
    source = "\n".join(f.readlines())
    print(SimpleDis()(source))
