import logging
import PIL
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import pathlib
import random
from pathlib import Path


logger = logging.getLogger()

def add_text_to_image(
        text,
        text_position=(10, 10),
        font_path=None,
        font_size=50,
        font_color=(255, 255, 255),
        input_image=None,
        output_image_path=None,
        img_x=128,
        img_y=250,
        vertical=True):
    if type(input_image) in (str, pathlib.WindowsPath, pathlib.Path, pathlib.PosixPath):
        # Open the input image
        image = Image.open(input_image)
    elif type(input_image) is PIL.PngImagePlugin.PngImageFile:
        image = input_image
    elif input_image is None:
        image = Image.new("RGB", (img_x, img_y), (255, 255, 255))
    else:
        raise Exception(f"Unrecognized image type: {type(input_image)}")
    draw = ImageDraw.Draw(image)

    # Load a font (you can specify the font path if needed)
    font = ImageFont.truetype(
        font_path, font_size) if font_path else ImageFont.load_default()

    # font = ImageFont.truetype("arial", size=font_size)

    # Specify the position and color of the text
    x, y = text_position
    r, g, b = font_color

    # Add the text to the image
    if vertical:
        # total_height = len(text) * font_size
        text_width, text_height = draw.textsize(text, font=font)
        # logger.info(f"total height is {total_height} px; lentext {len(text)} * font size {font_size}")
        # Create a new blank image to hold the vertical text
        vertical_text_image = Image.new(
            "RGB", (text_width, text_height), color=(255, 255, 255))
        vertical_draw = ImageDraw.Draw(vertical_text_image)

        # Paste each character vertically onto the new image
        vertical_draw.text((0, 0), text, fill=(r, g, b), font=font)
        # for char in text:
        #     char_width, char_height = draw.textsize(char, font=font)
        #     y += char_height  # Move to the next vertical position for the next character

        # Rotate the new image by 90 degrees
        vertical_text_image = vertical_text_image.rotate(90, expand=True)

        # Paste the vertical text image onto the original image
        # recalculate x, y
        ny = img_y - text_width + y
        image.paste(vertical_text_image, (x, ny))

    else:
        draw.text((x, y), text, fill=(r, g, b), font=font)

    logger.debug("Text added to the image successfully!")
    # Save the modified image to the output path
    if output_image_path:
        image.save(output_image_path)
    return image