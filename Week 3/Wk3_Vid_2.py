# import modules
import board
import time
import analogio
import neopixel
from simpleio import map_range

# declare objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analong input
analog_in = analogio.AnalogIn(board.A6)


# declare color variable & fill the pixels with the colors
color = (0,0,0)
pixels.fill(color)

# a smooth value for our smooth function
smooth_val = analog_in.value

# make a function to do a weighted average
def weightedSmooth(in_val, weight):
    # weight float between 0.0 and 1.0
    # in_value is the current reading of a shaky signal
    #reference smooth_valu as a global variable
    global smooth_val
    # apply weight to in_val and remaining weight to the output
    smooth_val = weight * in_val + ((1-weight) * smooth_val)
    return smooth_val


# repeat this code 4eva
while True:

    reading = analog_in.value

    smooth_val = weightedSmooth(reading, 0.1)



    # bit shift scale 16-bit to 8-bit value
    scaled_val = map_range(smooth_val, 0, 65535, 0, 255)
    scaled_val = int(scaled_val)
    print((smooth_val, reading))


    color = (0, scaled_val, scaled_val)

    pixels.fill(color)

    time.sleep(0.01)
