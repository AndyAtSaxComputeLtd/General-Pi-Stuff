#!/usr/bin/env python
try:
    import unicornhathd as hat
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as hat

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
	for x in range(0,8):
		if binary_str[x] == '1':
			hat.set_pixel(8-x, row, color[0], color[1], color[2])
		else:
			hat.set_pixel(8-x, row, 0, 0, 0)

while True:
    t = datetime.datetime.now()
    display_binary(10, t.year % 100, year_color)
    display_binary(11, t.month, month_color)
    display_binary(12, t.day, day_color)
    display_binary(13, t.hour, hour_color)
    display_binary(14, t.minute, minute_color)
    display_binary(15, t.second, second_color)
    hat.rotation(270)
    hat.show()
    time.sleep(1)
