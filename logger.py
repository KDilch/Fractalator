import logging
import logging.handlers
import os

from constants import APP_DIRS, LOG_FORMATTER, LOG_FILE_NAME


def set_log_level(log_level):
    """Source - python documentation: https://docs.python.org/2/howto/logging.html"""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)
    logging.getLogger().setLevel(numeric_level)


class Logger(object):
    """Class for handling setup of the logging to a file (log_level, name, fileHandler)"""

    def __init__(self, name):
        self.__name = name
        self.__create_log_dir()
        self.__add_rotating_file_handler()

    def __add_rotating_file_handler(self):
        """Creates a logger if doesn't exist already and appends to _LOGGERS list"""
        logger = logging.getLogger(self.__name)
        file_handler = logging.handlers.RotatingFileHandler(os.path.join(APP_DIRS.user_log_dir + LOG_FILE_NAME),
                                                            mode='a',
                                                            maxBytes=5*1024*1024,
                                                            backupCount=5)
        file_handler.setFormatter(LOG_FORMATTER)
        logger.addHandler(file_handler)

    @staticmethod
    def __create_log_dir():
        if not os.path.exists(APP_DIRS.user_log_dir):
            os.makedirs(APP_DIRS.user_log_dir)

    def debug(self, message):
        logging.getLogger(self.__name).debug(message)

    def info(self, message):
        logging.getLogger(self.__name).info(message)

    def warn(self, message):
        logging.getLogger(self.__name).warn(message)

    def error(self, message):
        logging.getLogger(self.__name).error(message)

    def critical(self, message):
        logging.getLogger(self.__name).critical(message)
