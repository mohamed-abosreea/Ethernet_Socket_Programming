import socket
import threading

# Client configuration
SERVER_HOST = '192.168.1.3'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Function to send messages
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Function to receive messages
def receive_message():
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if not message:
                break
            print(message.decode('utf-8'))
        except:
            break

# Create two threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
