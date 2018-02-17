#!/usr/bin/env python3

import os

def main():
    receive_ip = os.environ.get("RECV_IP")
    receive_port = int(os.environ.get("RECV_PORT"))
    if (receive_ip is None) or (receive_port is None):
        raise Exception("IP address was not provided")

    while True:
        message = input("MSG: ")

