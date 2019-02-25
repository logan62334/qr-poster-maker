#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    agent
    ~~~~~~~~~~~~

    This module is the main config.

    :copyright: (c) 2017 by Ma Fei.
"""
from logging.config import dictConfig

__version__ = '1'

LOGGING_CONFIG = dict({
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'qpagent': {
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
    },
    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    }
})
dictConfig(LOGGING_CONFIG)
