#Ashish Baby
#Version 1.00
#10-1-16

from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0,0,0)


def doors_unlock():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    G, G, G, G, G, G, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, G, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
  

images = [doors_unlock]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
