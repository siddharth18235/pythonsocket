import socket

HEADER = 64
PORT = 5050

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect..."
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("HELLLLLOOOOO !!!!")
send("HELLLLLOOOOO 1 !!!!")
send("HELLLLLOOOOO 2 !!!!")
send("HELLLLLOOOOO 3 !!!!")
send(DISCONNECT_MESSAGE)
