import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

data = sk.recv(1024)
sk.send(b'hi')
sk.close()