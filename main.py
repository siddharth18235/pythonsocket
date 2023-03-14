import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.29.2"
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect..."
# # printing of teh port and the hostanme : 
# print(SERVER)
# print(PORT)
# print(socket.gethostname())

ADDR = (SERVER, PORT)

# make of the socket: 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)

def handleClinet(conn, addr):
    # handle the indivisual connection between the cient and the server: 
    print(f"[NEW CONNECTION] :  {addr} connected ")
    connected = True
    while connected:
        # tells the length of the message : 
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            #  receives the msg: 
            msg = conn.recv(msgLength).decode(FORMAT)
            if (msg == DISCONNECT_MESSAGE):
                connected = False
            print(f"[{addr} : ] {msg}")
            conn.send("Message received : ".encode(FORMAT))
    
    conn.close()




        


def start():
    # allow the server to listen to connection: 
    # handle the connections and pass the connections to the handle_connections

    server.listen()
    print(f"SERVER IS LISTENING ON  {SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handleClinet, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS : ] {threading.activeCount()-1}")

print("Server is Starting...")
start()

