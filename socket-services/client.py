
import socket

HOST = "127.0.0.1"
PORT = 65500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        input_string = input("Message to send: ")
        
        if input_string == "END":
            break

        s.sendall(input_string.encode())

        data = s.recv(1024)
        print(f"Received {data.decode()}")
