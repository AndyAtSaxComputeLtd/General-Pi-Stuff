
buf_black        = bytearray(EPD_WIDTH * EPD_HEIGHT // 8) # used by frame buffer (landscape)
buf_epaper_black = bytearray(EPD_WIDTH * EPD_HEIGHT // 8) # used to display on e-paper after bytes have been oved from frame buffer to match e-paper (portrait) 

import framebuf
fb_black = framebuf.FrameBuffer(buf_black, EPD_WIDTH, EPD_HEIGHT, framebuf.MONO_VLSB)
BLACK = 0 # will be black on buf_black, red on buf_red
WHITE = 1

#clear red & black screens, write in black on top left and in red bootom right 
fb_black.fill(WHITE)
fb_black.text('Hello world!', 0, 0, BLACK)
