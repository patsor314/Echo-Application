import socket
import logging
import logging.config
import argparse

from utils.constants import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('CLIENT')

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', nargs='?', default='127.0.0.1', help="Specify hostname for server")
parser.add_argument('--port', nargs='?', type=int, default=65500, help="Specify hostname for server")
args = parser.parse_args()

host = args.hostname
port = args.port

print("Starting client")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

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
