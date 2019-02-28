#!/usr/bin/python3

import pika
import random
import time
import socket
import sys
import psycopg2

def is_open(addr, port, timeout=10):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((addr, int(port)))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return True
    except OSError as err:
        print(err)
        time.sleep(timeout)
        return False

def wait_until_available(addr, port, timeout=10):
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

if not wait_until_available("postgres", 5432):
    sys.exit(1)

db_conn = psycopg2.connect(host="postgres", database="postgres", user="postgres", password="postgres")
db_cur = db_conn.cursor()
db_cur.execute("CREATE TABLE IF NOT EXISTS recv_values (id SERIAL PRIMARY KEY, recv_value INT)")
db_cur.close()
db_conn.commit()
sql_query = "INSERT INTO recv_values (recv_value) VALUES (%s)"

conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
chan = conn.channel()

chan.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(' [x] Recieved', body)
    cur = db_conn.cursor()
    cur.execute(sql_query, (int(body),))
    cur.close()
    db_conn.commit()
    print(' [x] Added to database')

chan.basic_consume(callback, queue='hello', no_ack=True)
chan.start_consuming()
