import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print(f"The Server is listening for request on port <{port}>")

con, address = s.accept()

print(f"Connection has been established from <{str(address)}>")

try:
    fileName = con.recv((1024))
    file = open(fileName, 'rb')
    readFile = file.read()
    con.send(readFile)
    file.close()
    con.close()
    
except:
    con.send("File NOT found on the Server".encode())
