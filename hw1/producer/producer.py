#!/usr/bin/python3

import pika
import random
import time
import socket
import sys

def is_open(addr, port, timeout=10):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((addr, int(port)))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return True
    except:
        time.sleep(timeout)
        return False

def wait_until_available(addr, port, timeout=5):
    i = 0
    while True:
        i += 1
        print("Attempt #{} connecting to {}:{}".format(i, addr, port))
        if is_open(addr, port, timeout):
            print("Success")
            return True
        else:
            print("Failure")
    return False

if not wait_until_available("rabbitmq", 5672):
    sys.exit(1)

conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
chan = conn.channel()

chan.queue_declare(queue='hello')

while True:
    data = str(random.randint(1, 100))
    print("[x] sending", data)
    chan.basic_publish(exchange='', routing_key='hello', body=data)
    sleep_for = random.randint(1, 5)
    print("[x] Sleeping for", sleep_for, "seconds")
    time.sleep(sleep_for)
