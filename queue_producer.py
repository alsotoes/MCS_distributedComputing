#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import stomp
import random

def main():
    server = "localhost"
    port = 61613
    queue = "springfield"

    conn = stomp.Connection([(server, port)])
    conn.start()
    conn.connect('admin', 'password', wait=True)

    print("[+] Sending message in {} queue".format(queue))
    for count in range(int(sys.argv[1])):
        value = str(random.randrange(100))
        conn.send(body=value, destination='/queue/'+queue)
        print(" --> sended message {}".format(value))

    conn.disconnect()

# Start program
if __name__ == "__main__":
    main()
