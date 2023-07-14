# NOTE: This is just for dbg
from logging import basicConfig as __basicConfig, debug as __debug, DEBUG as __DEBUG
from typing import Any
__basicConfig(level=__DEBUG,
              format='%(asctime)s - %(levelname)s -> Hilo: %(threadName)s - Mensaje: %(message)s')


def dbg(*message: object):
    message = list(message)
    for index in range(len(message)):
        message[index] = str(message[index])

    __debug(msg=str('\t'.join(message)))
