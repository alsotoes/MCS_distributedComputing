#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import stomp
import random

server = "localhost"
port = 61613

def connect_and_subscribe(conn, topic):
    #topic = random.choice(['homero', 'bart', 'lisa'])
    #print("[+] Using topic: {}".format(topic))

    conn.start()
    conn.connect('admin', 'password', wait=True)
    conn.subscribe(destination='/topic/'+topic, id=1, ack='auto')

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn, topic):
        self.conn = conn
        self.topic = topic

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print(' received a message {}'.format(message))

    def on_disconnected(self):
        print('disconnected')
        connect_and_subscribe(self.conn, self.topic)


def main():
    server = "localhost"
    port = 61613
    topic = str(sys.argv[1])

    print("[+] Using topic: {}".format(topic))
    conn = stomp.Connection([(server, port)])
    conn.set_listener('', MyListener(conn, topic))
    connect_and_subscribe(conn, topic)

    time.sleep(1000)
    conn.disconnect()

# Start program
if __name__ == "__main__":
    main()
