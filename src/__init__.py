from .logdef import get_logger
from .draw_image import add_text_to_image

try:
    from .Epaper import *
except Exception as e:
    print('import error')
    print(e)
