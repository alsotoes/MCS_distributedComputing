#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import stomp
import random

def main():
    server = "localhost"
    port = 61613

    conn = stomp.Connection([(server, port)])
    conn.start()
    conn.connect('admin', 'password', wait=True)

    for count in range(int(sys.argv[1])):
        topic = random.choice(['homero', 'bart', 'lisa'])
        value = str(random.randrange(1000))
        conn.send(body=value, destination='/topic/'+topic)
        print("[+] Publishing message {} in {} topic".format(value, topic))

    conn.disconnect()

# Start program
if __name__ == "__main__":
    main()
