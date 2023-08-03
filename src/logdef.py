import sys
import logging
from datetime import datetime as dt


def get_logger(
        name,
        filedir='logs',
        ts_format='%Y-%m-%d_%H_%M_%S',
        level='info',
        format='%(asctime)s | %(levelname)s | %(message)s',
        to_console=True,
):
    lvl = {
        'critical': logging.CRITICAL, 'error': logging.ERROR,
        'warning': logging.WARNING, 'info': logging.INFO,
        'debug': logging.DEBUG, 'notset': logging.NOTSET,
    }.get(level, logging.INFO)
    logger = logging.Logger(
        level=lvl,
        name=name,
    )

    formatter = logging.Formatter(format)

    if filedir:
        ts = dt.now().strftime(ts_format)
        # print(f"{filedir}/{name}_{ts}.log")
        handler = logging.FileHandler(f"{filedir}/{name}_{ts}.log")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    if to_console:
        # writing to stdout
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
