# Write your code here :-)

# import modules
import board
import time
import touchio
import neopixel

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1-TX)
touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPin7 = touchio.TouchIn(board.TX)

# put pins in a list
touchPins = [touchPin1, touchPin2, touchPin3, touchPin4,
            touchPin5, touchPin6, touchPin7,]


touchVals = [False, False, False, False, False, False, False,]

# neopixel stuff
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
Color = (0, 25, 255)
Clear = (0, 0 ,0)

# repeat forever
while True:
    # print the value of the touchPin to serial
    for x in range(7):
        touchVals[x] = touchPins[x].value

    print(touchVals)

    for x in range(7):
        if touchVals[x] == True:
            pixels[x] = Color
        else:
            pixels[x] = Clear

    """
    # do neopixel output
    if touchVal:
        pixels.fill(Color)
    else:
        pixels.fill(Clear)
    """
    time.sleep(0.1)
