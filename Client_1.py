import pickle
import socket

HOST = (socket.gethostname(), 9999)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем связку ip и порт
client.connect(HOST)

print("Connect...", HOST)

requests = b'Hello, i Cavin'
client.sendall(requests)
