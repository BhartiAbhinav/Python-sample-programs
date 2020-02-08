import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))

s.listen((5))
while True:
    c,addr=s.accept()
    print("Got connection from",addr)
    c.send(bytes("Thank you for connecting","utf-8"))
    c.close()