# import modules
import board
import time
import analogio
import neopixel
from simpleio import map_range
import adafruit_fancyled.adafruit_fancyled as fancy

# declare objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analong input
force = analogio.AnalogIn(board.A6)
photo = analogio.AnalogIn(board.A5)
flex = analogio.AnalogIn(board.A1)


# declare color variable & fill the pixels with the colors


# a smooth value for our smooth function





# repeat this code 4eva
while True:

    sat = force.value
    hue = flex.value
    bright = photo.value


    satScaled = map_range(sat, 0, 64000, 255, 0)
    satScaled = int(satScaled)

    hueScaled = map_range(hue, 6000, 17000, 0, 255)
    hueScaled = int(hueScaled)

    brightScaled = map_range(bright, 10000, 62500, 0, 255)
    brightScaled = int(brightScaled)


    # calls for HSV values
    color = fancy.CHSV(hueScaled, satScaled, brightScaled)
    # converts float HSV values to integer RGB values
    packed = color.pack()
    # writes converted int values to NeoPixels
    pixels.fill(packed)



    print(satScaled)

    time.sleep(0.1)
