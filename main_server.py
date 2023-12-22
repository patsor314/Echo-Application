import sys
import socket
import selectors
import types
import logging
import logging.config
import argparse

from socket_services.MultiConnectionServer import MultiConnectionServer
from utils.log import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('SERVER')

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', nargs='?', default='127.0.0.1', help="Specify hostname for server")
parser.add_argument('--port', nargs='?', type=int, default=65500, help="Specify hostname for server")
args = parser.parse_args()

host = args.hostname
port = args.port

server = MultiConnectionServer(host, port)
server.receive_connections()
