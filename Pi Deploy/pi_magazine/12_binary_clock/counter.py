#!/usr/bin/env python

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

hat.clear()
hat.brightness(0.5)

def display_binary(row, value, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color[0], color[1], color[2])
		else:
			hat.set_pixel(x, row, 0, 0, 0)

t = datetime.datetime.now()
display_binary(0, 1, year_color)
display_binary(1, 2, year_color)
display_binary(2, 4, year_color)
display_binary(3, 8, year_color)
display_binary(4, 16, year_color)
display_binary(5, 32, year_color)
display_binary(6, 64, year_color)
display_binary(7, 128, year_color)
display_binary(8, 256, year_color)
display_binary(9, 512, year_color)
display_binary(10, 1024, year_color)
display_binary(11, 2048, year_color)
display_binary(12, 4096, year_color)
display_binary(13, 8192, year_color)
display_binary(14, 16384, year_color)
display_binary(15, 32768, year_color)
hat.show()

