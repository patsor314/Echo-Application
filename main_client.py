import socket
import logging
import logging.config

from utils.constants import HOSTNAME, HOST_PORT, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('CLIENT')

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
