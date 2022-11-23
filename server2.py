import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    if data == (bytes('Hi',encoding='UTF-8')) or data == (bytes('Hello',encoding='UTF-8')):
       print(bytes('Whats up',encoding='UTF-8'))
    else:
        print(bytes('I dont understand',encoding='UTF-8'))
    print(str(data))
    conn.send(data.upper())
conn.close()

