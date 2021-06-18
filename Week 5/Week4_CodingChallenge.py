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

# values for toggle to work
ledMode = 0
preTouchVal = False

# red values
redVal = 1
redStep = 10

# blue values
blueVal = 1
blueStep = 10

# green values
greenVal = 1
greenStep = 10

Color = (redVal, blueVal, greenVal)
Clear = (0, 0 ,0)

# repeat forever
while True:
    # print the value of the touchPin to serial
    for x in range(7):
        touchVals[x] = touchPins[x].value

        if touchVals[0] != preTouchVal:
            preTouchVal = touchVals[0]
            if touchVals[0]:
                ledMode += 1
                if ledMode > 1:
                    ledMode = 0

    # toggle on with A1
    if ledMode == 1:
        pixels.fill(Color)
        # increase value of red with A2
        if touchVals[1] == True:
            if redVal < 250:
                redVal = redVal + redStep
                Color = (redVal, blueVal, greenVal)

            elif redVal > 255:
                redVal = 255

        # decrease value of red with A3
        if touchVals[2] == True:
            if redVal > 1:
                redVal = redVal - redStep
                Color = (redVal, blueVal, greenVal)

            else:
                redVal = 1
        # increase value of blue with A4
        if touchVals[3] == True:
            if blueVal < 250:
                blueVal = blueVal + blueStep
                Color = (redVal, blueVal, greenVal)

            elif blueVal > 255:
                blueVal = 255

        # decrease value of blue with A5
        if touchVals[4] == True:
            if blueVal > 1:
                blueVal = blueVal - blueStep
                Color = (redVal, blueVal, greenVal)

            else:
                blueVal = 1
        # increase value of green with A6
        if touchVals[5] == True:
            if greenVal < 250:
                greenVal = greenVal + greenStep
                Color = (redVal, blueVal, greenVal)

            elif greenVal > 255:
                greenVal = 255

        # decrease value of green with TX
        if touchVals[6] == True:
            if greenVal > 1:
                greenVal = greenVal - greenStep
                Color = (redVal, blueVal, greenVal)
                print(greenVal)

            else:
                greenVal = 1
                print(greenVal)
    else:
        pixels.fill(Clear)





    time.sleep(0.1)
