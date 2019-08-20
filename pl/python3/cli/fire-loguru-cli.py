#!/usr/bin/env python3

import sys
from loguru import logger
# TODO mike@carif.io https://buildmedia.readthedocs.org/media/pdf/loguru/stable/loguru.pdf, https://github.com/Delgan/loguru
# Make 'WARNING' the default level by removing the default handler and adding a "warning" one. Hacky.
default_log_level = 'WARNING'
logger.remove()
logger.add(sys.stderr, format="{time} {level} {message}", filter=__name__, level=default_log_level)

import inspect  # me()
import fire  # https://github.com/google/python-fire

def me():
    """
    Returns the name of the function this is called in, e.g. def foo: return me() => 'foo'
    :return: str
    """
    return inspect.stack()[1][3]

def main(level=default_log_level):
    if level != default_log_level:
        logger.remove()
        logger.add(sys.stderr, format="{time} {level} {message}", filter=__name__, level=level)
    logger.debug(me())

# Lot of work to get here
if '__main__' == __name__:
    fire.Fire(main)

