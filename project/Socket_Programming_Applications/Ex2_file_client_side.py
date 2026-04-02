import socket

s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))

fileName = input("Enter the filename you want to display its content --> ")

s.send(fileName.encode())

readfile = s.recv(1024)

print("\n" + readfile.decode())

s.close()
