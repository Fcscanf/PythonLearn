import socket
s = socket.socket()
s.connect(('119.29.231.174', 22))
s.send("Primal Security \n".encode())
banner = s.recv(1024)
print(banner)