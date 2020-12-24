import socket

## Define a socket object and enable connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    ## Accept the conection
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been establihed.")
    ## Send information to the client
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    ##Close connection
    clientsocket.close()
