"""
# General-purpose simple logging script.

The function below handles all the main default settings for a logging script, such as:
- where to save the logging outputs
- whether to print the logging outputs to console

## Usage
### Main script:
- import logdef.getlogger on your main module
- call `logger = get_logger()` with or without the default settings
### Secondary modules/scripts:
- import logging
- call `logger = logging.getLogger(__main__)`

In both cases, `logger.info/debug/warning()` will display the information to the file and/or the console

"""
import sys
import logging
from datetime import datetime as dt


def get_logger(
        name,
        level='info',
        filedir="logs",
        ts_format='%Y-%m-%d_%H_%M_%S',
        log_format='%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(message)s',
        to_console=True,
        console_format=None,
):
    lvl = {
        'critical': logging.CRITICAL, 'error': logging.ERROR,
        'warning': logging.WARNING, 'info': logging.INFO,
        'debug': logging.DEBUG, 'notset': logging.NOTSET,
    }.get(level, logging.INFO)

    ts = f"_{dt.today().strftime(ts_format)}"

    logging.basicConfig(
        level=lvl,
        format=log_format, 
        filename=f"{filedir}/{name}{ts}.log",
        filemode='a',
    )


    if to_console:
        formatter = logging.Formatter(console_format if console_format else log_format)
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    return logging.getLogger(name)
