import socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
comment = input(' ')
sock.send(bytes(comment, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)