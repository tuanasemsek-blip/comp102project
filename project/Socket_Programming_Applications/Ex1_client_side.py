import socket

s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))
message = s.recv(1024)

while message:
    print(f"Message --> {message.decode()}")
    message = s.recv(1024)
    
s.close()
