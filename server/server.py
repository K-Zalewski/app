#!/usr/bin/env python3

import socket

TCP_PORT = 1234
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)
s.settimeout(30)

conn, addr = s.accept()

while 1:
	try:
		data = conn.recv(BUFFER_SIZE)
		if data:
			print(data.decode())
		else:
			print("Client closed the connection.")
			break
	except socket.timeout:
		print("Timed out - no more responses.")
		break

conn.close()
s.close()
