import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)
conn,_ = sk.accept()
conn.send(b'Hi')
data = conn.recv(1024)
print(data)
conn.close()
sk.close()