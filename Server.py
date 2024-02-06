import pickle
import socket

HOST = (socket.gethostname(), 9999)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем связку ip и порт
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # очистка порта для его переисользования

s.bind(HOST)
s.listen()
print("Cервер работает")

while True:
    client, address = s.accept()
    print("connected - ", address)
    req = b''
    while True:
        data = client.recv(1024)
        if not len(data):
            break
        req += data
    print(req.decode('utf-8'))
    client.close()
