# import modules
import board
import time
import analogio
import neopixel
from simpleio import map_range
# declare objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
ledMode = 0
preReading = False
reading = False

# declare analong input
force = analogio.AnalogIn(board.A1)
photo = analogio.AnalogIn(board.A2)


# declare color variable & fill the pixels with the colors
LightOn = (255, 255, 255)
LightOff = (0, 0, 0)
# a smooth value for our smooth function


# repeat this code 4eva
while True:

    forceInput = force.value
    if forceInput > 10000:
        reading = not reading
        if reading != preReading:
                preReading = reading
                if reading:
                    ledMode += 1
                    if ledMode > 1:
                        ledMode = 0


    print(ledMode)

    if ledMode == 1:
        pixels.fill(LightOn)
    else:
        pixels.fill(LightOff)

    time.sleep(0.1)
