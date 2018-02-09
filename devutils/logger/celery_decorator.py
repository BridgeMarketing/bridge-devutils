from functools import wraps, update_wrapper
from celery.utils.log import get_task_logger

from logstash_logger import LogstashLogger

def set_logger(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        tid = 'unknown'
        pid = 'unknown'
        try:
            j = request.json
            pid = kwargs['newState']['projectID']
            tid = kwargs['newState']['ID']
        except Exception as e:
            pass

        logger = get_task_logger(__name__)
        logger = LogstashLogger(logger,
            parameters={
            'projectID': pid,
            'taskID': tid,
            'function': '%s.%s' % (f.__module__, f.func_name),
        })
        args = args + (logger, )
        return f(*args, **kwargs)
    decorated_function.__doc__ = f.__doc__
    decorated_function.__name__ = f.__name__
    return decorated_function

