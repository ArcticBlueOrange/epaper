from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

# Path to the Liberation Sans font file on your system
# font_path = "LiberationSans-Regular.ttf"

def extract_font_info(font_path):
    try:
        font = TTFont(font_path)
        font_info = font['name'].names

        for record in font_info:
            if record.nameID == 1:
                print(f"Font Family: {record.string.decode('utf-8')}")
            elif record.nameID == 4:
                print(f"Font Full Name: {record.string.decode('utf-8')}")

        font.close()
    except Exception as e:
        print(f"Error: {e}")

# Extract font information


# font = ImageFont.truetype(
    # font_path, font_size) if font_path else ImageFont.load_default()


if __name__ == "__main__":

    while True:
        f = input("Please insert a font name")
        if f == '0':
            break
        extract_font_info(f)



