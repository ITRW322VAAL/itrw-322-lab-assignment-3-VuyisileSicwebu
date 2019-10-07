#!/usr/bin/env python3

import socket

host = '127.0.0.1' # The server's hostname or IP address
port = 9999       # The port used by the srever

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello, Server')
    data = s.recv(1024)
       
print('Received', repr(data))