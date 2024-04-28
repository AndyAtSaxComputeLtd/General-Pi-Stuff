#!/usr/bin/env python
import socket
import unicornhathd as hat
import time, datetime

year_color = (0, 255, 0)
month_color = (0, 0, 255)
day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundrefths_color = (127, 127, 0)
off = (0, 0, 0)

hat.brightness(0.5)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

def display_binary(row, value, color):
        binary_str = "{0:8b}".format(value)
        for x in range(0, 8):
                if binary_str[x] == '1':
                        hat.set_pixel(8 - x, row, color[0], color[1], color[2])
                else:
                        hat.set_pixel(8 - x, row, 0, 0, 0)

def get_ip():
    # get IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    my_ip = s.getsockname()[0]
    print(my_ip)
    s.close()
    return my_ip


def create_image_from_text(in_text):
    colours = (255, 255, 250)
    # font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
    font_file = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
    font_size = 8
    font = ImageFont.truetype(font_file, font_size)
    w, h = font.getsize(in_text)

    text_x, text_y = width, 0
    text_width, text_height = width, 0

    text_width += w + width                # add some padding so the ip scrolls off the unicorn hat
    text_height = max(text_height, h, 16)  # no more than the size of the unicorn hat

    image = Image.new('RGB', (text_width, text_height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), in_text, colours, font=font)
    return (image, text_width)


# DISPLAY
def scroll_txt(image, text_width):
    hat.rotation(90)
    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x + scroll, y))
                r, g, b = [int(n) for n in pixel]
                hat.set_pixel(width - 1 - x, y, r, g, b)

                # display binary clock
                t = datetime.datetime.now()
                display_binary(10, t.year % 100, year_color)
                display_binary(11, t.month, month_color)
                display_binary(12, t.day, day_color)
                display_binary(13, t.hour, hour_color)
                display_binary(14, t.minute, minute_color)
                display_binary(15, t.second, second_color)
        hat.show()
        time.sleep(0.02)
    # hat.off()


# one stop call for scrolling text
def scroll_text(in_txt):
    image, text_width = create_image_from_text(in_txt)
    scroll_txt(image, text_width)


if __name__ == '__main__':
    width, height = hat.get_shape()  # 16, 16 by default
    my_ip = get_ip()
