import logging

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] - %(name)s: %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z'
        },
        'simple': {
            'format': '%(message)s',
        }
    },
    'handlers': {
        'server': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': f'logs/server.log',
            'mode': 'a'
        },
        'client': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': f'logs/client.log',
            'mode': 'a'
        },
        'stdout': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        'CLIENT': {
            'handlers': ['client', 'stdout'],
            'level': 'DEBUG',
            'propagate': False
        },
        'SERVER': {
            'handlers': ['server', 'stdout'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
