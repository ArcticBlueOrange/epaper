# In[1]:
import PIL
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import pathlib
import random
from pathlib import Path
IMG_PATH = Path('images')

from src import *
logger = get_logger(
    "epaper", 'debug',
    console_format="%(asctime)s | %(message)s" )
# In[10]:
# Example usage:
# input_image_path = IMG_PATH / 'red.png'
output_image_path = IMG_PATH / "output_image.png"
font_size = 10

img0 = base_image(COLOR.RED)
logger.debug(type(img0))
img1 = add_text_to_image(
    text=f"test {random.randint(0,1000)}",
    text_position=(2,2),
    font_path='bahnschrift.ttf',
    font_size=font_size,
    font_fg=COLOR.RED,
    font_bg=COLOR.BLACK,
    
    input_image=img0)
logger.debug(type(img1))
img2 = add_text_to_image(
    text=f"test {random.randint(0,1000)}",
    text_position=(10, 2),
    font_path='bahnschrift.ttf',
    font_size=font_size,
    font_fg=COLOR.BLACK,
    font_bg=COLOR.RED,
    input_image=img1,
    output_image_path=output_image_path,
)
img3 = add_text_to_image(
    text=f"test {random.randint(0,1000)}",
    text_position=(16, 2),
    font_path='bahnschrift.ttf',
    font_size=font_size,
    font_fg=COLOR.WHITE,
    font_bg=COLOR.RED,
    input_image=img1,
    output_image_path=output_image_path,
)
img3
# In[6]:
data = img2.load()
X_PIXEL = 128
Y_PIXEL = 250

rBuf = [0] * 4000
bBuf = [0] * 4000

e = Epaper(X_PIXEL,Y_PIXEL)

for y in range(250):
    for x in range(128):
       # Red CH
       if data[x,y] == (237,28,36):
           # This algorithm has bugs if ported according to C, the solution is referred to:https://www.taterli.com/7450/
           index = int(16 * y + (15 - (x - 7) / 8))
           tmp = rBuf[index]
           rBuf[index] = tmp | (1 << (x % 8))
       # Black CH
       elif data[x,y] == (255,255,255):
            index = int(16 * y + (15 - (x - 7) / 8))
            tmp = bBuf[index]
            bBuf[index] = tmp | (1 << (x % 8))

logger.debug("Pasting image to screen")

e.flash_red(buf=rBuf)
e.flash_black(buf=bBuf)
e.update()
