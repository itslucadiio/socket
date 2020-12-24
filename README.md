<h2 align="center">Using socket</h2>

We will use Socket to create a connection from a server to a client. The server is going to send a message that the client will recieve. 

## First socket
### Server.py
````python
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
    ## Close connection
    clientsocket.close()
````

### Client.py
````python
import socket

## Define a socket object and enable connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

## Data buffer 
fullMsg = ''
while True:
    ## Recives the message by lengths of 8 until the mesage 
    ## length is zero (break), then prints the full message.
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    fullMsg += msg.decode("utf-8")

print(fullMsg)
````

## Upgrades

To avioid force-closing the server in order to recieve the message correctly, we will use a fixed-length header with the length of the message sent.

### Server.py
````python
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
````

### Client.py
````python
import socket

HEADERSIZE = 10

## Define a socket object and enable connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

## Data buffer 
while True:
    fullMsg = ''
    newMsg = True
    while True:
        msg = s.recv(16)
        ## When its a new message
        if newMsg:
            print(f'new message of length {len(msg[:HEADERSIZE])}')
            msgLen = int(msg[:HEADERSIZE])
            newMsg = False
        fullMsg += msg.decode("utf-8")
        ## When the full message is recived
        if len(fullMsg)-HEADERSIZE == msgLen:
            print("full msg recived")
            print(fullMsg[HEADERSIZE:])
            fullMsg = ''
            newMsg = True

````

