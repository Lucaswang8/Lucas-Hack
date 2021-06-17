# Week 4 Video - List with Lights

# import modules
import board
import time
import neopixel

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# declare a list of 10 fading cotton candy color tuples
# this is also known as a lookup table
colors = [(0, 255, 0), (28, 277, 0),
         (56, 199, 0), (84, 171, 0),
         (112, 143, 0), (140, 115, 0),
         (168, 87, 0), (196, 59, 0),
         (224, 31, 0), (255, 0, 0)]

for x in range(len(pixels)):
    pixels[x] = colors[x]

pixels.show()

time.sleep(1)

while True:
    # do calculations
    popColor = colors.pop(0)

    colors.append(popColor)

    for x in range(len(pixels)):
        pixels[x] = colors[x]

    pixels.show()

    time.sleep(0.1)


    # do output


