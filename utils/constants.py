import logging

HOST_PORT=65500
HOSTNAME='127.0.0.1'

LOGGING_CONFIG = {
    'format': '%(asctime)s [%(levelname)s] - %(name)s: %(message)s',
    'datefmt': '%Y-%m-%dT%H:%M:%S%z',
    'level': logging._nameToLevel['DEBUG']
}
