import socket

HEADERSIZE = 10

## Define a socket object and enable connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    ## Accept the conection
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been establihed.")
    ## Send information to the client
    ## The msg corresponds to a fixed-length header of legth 10 and the actual message
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))
