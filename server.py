import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "[AVKOBLET]"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
#allclients = []

def handle_client(conn, addr):
    print(f"[NY TILKOBLING] {addr} tilkoblet.")
    
    #broadcast(addr)
    #allclients.append(conn)
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
        
            print(f"[{addr}] {msg}")
            conn.send(f"Melding '({msg})' mottatt".encode(FORMAT))
        
    conn.close()
    
#def broadcast(bruker):
   #for client in allclients:
       #client.send(f"Nå har bruker {bruker} koblet seg til serveren!".encode(FORMAT))
    
def start():
    server.listen()
    print (f"[LYTTER] Serveren lytter på ip-adresse {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        #broadcast(addr)
        #allclients.append(conn)
        print(f"Tilkoblede brukere: {allclients}")
        thread.start()
        print(f"[AKTIVE TILKOBLINGER] {threading.activeCount() - 1}")
        
print ("[STARTER] Serveren starter...")
start()



