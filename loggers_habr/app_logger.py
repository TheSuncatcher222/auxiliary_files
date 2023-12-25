import logging
import sys

FORMAT = (
    '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s'
    +'(%(lineno)d) - %(message)s'
)
FORMATTER = logging.Formatter(FORMAT)


def get_stream_handler():
    stream_handler = logging.StreamHandler(stream=sys.stderr)
    stream_handler.setFormatter(FORMATTER)
    return stream_handler


def get_file_handler():
    file_handler = logging.FileHandler("log.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())

    return logger
