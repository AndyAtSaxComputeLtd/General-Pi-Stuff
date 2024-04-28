# sudo apt-get install python-gpiozero python3-gpiozero
# This example sets all the red LEDs to flicker randomly:
# pip install gpiozero
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)
for led in tree:
 led.source_delay = 0.1
 led.source = random_values()
pause()