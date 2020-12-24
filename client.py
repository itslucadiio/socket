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
