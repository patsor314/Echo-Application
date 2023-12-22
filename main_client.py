import socket
import logging
import logging.config

from utils.constants import HOSTNAME, HOST_PORT, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('CLIENT')

print("Starting client")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOSTNAME, HOST_PORT))

    print("Connected to host. Type END to end connection.")
    while True:
        input_string = input("Message to send: ")

        if input_string == "":
            continue

        if input_string == "END":
            printf("Ending connection to host")
            break

        s.sendall(input_string.encode())

        data = s.recv(1024)
        logger.info(f"Received \'{data.decode()}\'")
