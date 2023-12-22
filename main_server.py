import sys
import socket
import selectors
import types
import logging
import logging.config

from socket_services.MultiConnectionServer import MultiConnectionServer
from utils.constants import HOSTNAME, HOST_PORT, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('server')

server = MultiConnectionServer()
server.receive_connections()
