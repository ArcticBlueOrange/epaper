import sys
import logging
from datetime import datetime as dt


def get_logger(
        name,
        level='info',
        filedir="logs",
        filename='epaper',
        ts_format='%Y-%m-%d_%H_%M_%S',
        text_format='%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(message)s',
        to_console=True,
        console_format=None,
):
    lvl = {
        'critical': logging.CRITICAL, 'error': logging.ERROR,
        'warning': logging.WARNING, 'info': logging.INFO,
        'debug': logging.DEBUG, 'notset': logging.NOTSET,
    }.get(level, logging.INFO)

    ts = dt.today().strftime(ts_format)

    logging.basicConfig(
        level=lvl,
        format=text_format, 
        filename=f"{filedir}/{name}_{ts}.log",
        filemode='a',
    )


    if to_console:
        formatter = logging.Formatter(console_format if console_format else text_format)
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    return logging.getLogger(name)
