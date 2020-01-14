import socket

HOST = "google.com"
PORT = 80
REQUEST = b'GET / HTTP/1.1\r\n\r\n'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(REQUEST)
    received = s.recv(1048).decode('ascii')
    print(received)