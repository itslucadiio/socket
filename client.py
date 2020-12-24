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

  