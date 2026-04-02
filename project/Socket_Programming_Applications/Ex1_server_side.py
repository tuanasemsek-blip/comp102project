import socket

host = 'localhost'
port = 8080
server_name = "COMP303"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
con, adress = s.accept()
print(f"Connection has been established from {str(adress)}")
con.send(f"Hello my name is {server_name} and I am the Server =)".encode())
con.close()
