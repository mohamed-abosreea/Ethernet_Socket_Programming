import socket
import threading

# Server configuration
HOST = '192.168.1.3'  # Listen on all available network interfaces
PORT = 12345
BUFFER_SIZE = 1024

# List to store client connections
clients = []

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Listen for up to 5 incoming connections

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send a message
                clients.remove(client)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if not message:
                break
            message = message.decode('utf-8')
            print(message)
            broadcast(message.encode('utf-8'), client_socket)
        except:
            # Remove the client if an error occurs
            clients.remove(client_socket)
            break

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Client {client_address} connected.")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
