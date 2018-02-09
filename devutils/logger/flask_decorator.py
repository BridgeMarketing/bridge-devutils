import logging
from logging.handlers import TimedRotatingFileHandler

from functools import wraps, update_wrapper

from flask import request

from logstash_logger import LogstashLogger

logger = None

def initialize_logger(*args, **kwargs):
    global logger
    logger = logging.getLogger(kwargs['logger_name'])
    logger.setLevel(kwargs['logger_level'])

    formatter = logging.Formatter("[%(asctime)s] %(message)s")
    handler = TimedRotatingFileHandler(
                    kwargs['logger_file_name'],
                    when='midnight',
                    backupCount=5,
                    utc=True)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def set_logger(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        tid = 'unknown'
        pid = 'unknown'
        try:
            j = request.json
            pid = j['newState']['projectID']
            tid = j['newState']['taskID']
        except Exception as e:
            pass
        l = LogstashLogger(logger,
            parameters={
            'projectID': pid,
            'taskID': tid,
        })
        args = args + (l, )
        return f(*args, **kwargs)
    decorated_function.__doc__ = f.__doc__
    decorated_function.__name__ = f.__name__
    return decorated_function

