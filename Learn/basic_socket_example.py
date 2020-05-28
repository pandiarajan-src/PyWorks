'''Basic socket example'''

import socket

SERVER_ADDR = input("What server do you want to connect to? ")
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.connect((SERVER_ADDR, 80))
SOCK.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(SERVER_ADDR, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
REPLY = SOCK.recv(10000)
SOCK.shutdown(socket.SHUT_RDWR)
SOCK.close()
print(repr(REPLY))
