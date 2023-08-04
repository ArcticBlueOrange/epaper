import logging
import PIL
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import pathlib
import random
from pathlib import Path

__all__ = [
    'COLOR',
    'add_text_to_image',
    'base_image',
]

IMG_X=128
IMG_Y=250

class COLOR:
    RED = (237,28,36)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

logger = logging.getLogger(__name__)

def add_text_to_image(
        text,
        text_position=(10, 10),
        font_path=None,
        font_size=50,
        font_fg=COLOR.BLACK,
        font_bg=COLOR.WHITE,
        input_image=None,
        output_image_path=None,
        img_x=IMG_X,
        img_y=IMG_Y,
        vertical=True):
    if type(input_image) in (str, pathlib.WindowsPath, pathlib.Path, pathlib.PosixPath):
        # Open the input image
        image = Image.open(input_image)
    elif input_image is None:
        image = Image.new("RGB", (img_x, img_y), COLOR.WHITE)
    else:
        image = input_image
    logger.debug(image)
    draw = ImageDraw.Draw(image)

    # Load a font (you can specify the font path if needed)
    font = ImageFont.truetype(
        font_path, font_size) if font_path else ImageFont.load_default()

    # font = ImageFont.truetype("arial", size=font_size)

    # Specify the position and color of the text
    x, y = text_position

    # Add the text to the image
    if vertical:
        text_width, text_height = draw.textsize(text, font=font)
        # Create a new blank image to hold the vertical text
        vertical_text_image = Image.new(
            "RGB", (text_width, text_height), color=font_bg)
        vertical_draw = ImageDraw.Draw(vertical_text_image)

        # Paste each character vertically onto the new image
        vertical_draw.text((0, 0), text, fill=font_fg, font=font)

        # Rotate the new image by 90 degrees
        vertical_text_image = vertical_text_image.rotate(90, expand=True)

        # Paste the vertical text image onto the original image
        # recalculate x, y
        ny = img_y - text_width - y
        image.paste(vertical_text_image, (x, ny))
    else:
        draw.text((x, y), text, fill=font_fg, font=font)

    logger.debug("Text added to the image successfully!")
    # Save the modified image to the output path
    if output_image_path:
        image.save(output_image_path)
    return image

def base_image(color:COLOR, size=(IMG_X, IMG_Y)):
    return Image.new("RGB", size=size, color=color)
