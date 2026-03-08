import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Connection closed")
            client.close()
            break

def send():
    while True:
        msg = input()
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())

thread = threading.Thread(target=receive)
thread.start()

send()