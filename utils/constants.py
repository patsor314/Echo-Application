import logging

HOST_PORT=65500
HOSTNAME='127.0.0.1'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] - %(name)s: %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z'
        }
    },
    'handlers': {
        'server': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': f'logs/server.log',
            'mode': 'a'
        },
        'client': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': f'logs/client.log',
            'mode': 'a'
        },
    },
    'loggers': {
        'CLIENT': {
            'handlers': ['client'],
            'level': 'DEBUG',
            'propagate': False
        },
        'SERVER': {
            'handlers': ['server'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
