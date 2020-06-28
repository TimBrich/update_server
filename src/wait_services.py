#!/usr/bin/env python
import socket
import time

print("Waiting postgres to launch on postgres:5432...\n")
while True:
    try:
        s = socket.create_connection(('postgres', 5432), 300)
        s.close()
        break
    except socket.error:
        pass
    print("wait for 1 of the second before check again\n")
    time.sleep(1)
print("postgres:5432 is acceptable.\n")
