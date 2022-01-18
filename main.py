import pandas
from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/Montserrat-Bold.ttf', 28)
FONT_COLOR = "#000000"

template = Image.open(r'CertificateTemplate.png')
WIDTH, HEIGHT = template.size


def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'CertificateTemplate.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text.
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 10), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name + ".png")
    print('Saving Certificate of:', name)


if __name__ == "__main__":

    names = []

    with open('names.txt') as f:
        content = f.readlines()
        for item in content:
            names.append(item[:-1].title())

    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
