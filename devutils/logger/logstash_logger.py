import json
import traceback

class LogstashLogger(object):

    def __init__(self, logger, parameters={}):
        self.logger = logger
        self.parameters = parameters

    def add_id(self, key, value):
        self.parameters[key] = value

    def build_message(self, msg, trace=''):
        if (not len(trace)) and ('traceback' in self.parameters):
            del self.parameters['traceback']
        elif len(trace):
            self.parameters['traceback'] = trace
        self.parameters['msg'] = str(msg)
        return json.dumps(self.parameters)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def debug(self, msg, *args, **kwargs):
        msg = self.build_message(msg)
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = self.build_message(msg)
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = self.build_message(msg)
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = self.build_message(msg)
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = self.build_message(msg)
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = self.build_message(msg, trace=traceback.format_exc())
        self.logger.error(msg, *args, **kwargs)

