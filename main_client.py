import socket
import logging

from utils.constants import HOSTNAME, HOST_PORT, LOGGING_CONFIG

logging.basicConfig(**LOGGING_CONFIG)
logger = logging.getLogger(__name__)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOSTNAME, HOST_PORT))

    while True:
        input_string = input("Message to send: ")

        if input_string == "":
            continue
            
        if input_string == "END":
            break

        s.sendall(input_string.encode())

        data = s.recv(1024)
        logger.info(f"Received \'{data.decode()}\'")
