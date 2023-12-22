import sys
import socket
import selectors
import types
import logging

from socket_services.MultiConnectionServer import MultiConnectionServer
from utils.constants import HOSTNAME, HOST_PORT, LOGGING_CONFIG

logging.basicConfig(**LOGGING_CONFIG)
logger = logging.getLogger(__name__)

server = MultiConnectionServer()
server.receive_connections()
