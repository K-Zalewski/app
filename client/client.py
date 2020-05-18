#!/usr/bin/env python3

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 1234
MESSAGE = "Hello!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
	try:
		s.send(str.encode(MESSAGE))
		time.sleep(3)
	except socket.error:
		print("Caught exception socket.error")
		break

s.close()
