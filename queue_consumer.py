#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import stomp

def connect_and_subscribe(conn, queue):
    conn.start()
    conn.connect('admin', 'password', wait=True)
    conn.subscribe(destination='/queue/'+queue, id=1, ack='auto')

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn, queue):
        self.conn = conn
        self.queue = queue

    def on_error(self, headers, message):
        print("received an error {}".format(message))

    def on_message(self, headers, message):
        print(" --> received a message {}".format(message))

    def on_disconnected(self):
        print("disconnected")
        connect_and_subscribe(self.conn, self.queue)

def main():
    server = "localhost"
    port = 61613
    queue = "springfield"

    conn = stomp.Connection([(server, port)])
    conn.set_listener('', MyListener(conn, queue))
    print("[+] Receiving message from {} queue".format(queue))
    connect_and_subscribe(conn, queue)
    time.sleep(1000)
    conn.disconnect()

# Start program
if __name__ == "__main__":
    main()
