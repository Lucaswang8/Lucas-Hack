# Write your code here :-)
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import analogio
import touchio

ring = touchio.TouchIn(board.TX)
pinkie = touchio.TouchIn(board.A6)
index = touchio.TouchIn(board.A1)

prevPinkie = False
prevRing = False

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

sensorMode = 0

while True:

    #assigning variables
    indexFinger = index.value
    currentRing = ring.value
    currentPinkie = pinkie.value

    #sensorMode Toggle
    if currentPinkie != prevPinkie :
        prevPinkie = currentPinkie
        if currentPinkie :
            sensorMode += 1
            if sensorMode > 1:
                sensorMode = 0


    #print(currentPinkie)
    #print(sensorMode)

    #sensorMode is On
    if sensorMode == 1:
        led.value = True


        if indexFinger == True:
            print("<index>")
        if currentRing != prevRing:
            prevRing = currentRing
            if currentRing:
                # start timer
                ringTapTime = time.monotonic()
                # check if it is long pressed
            else:
                print("short pressed")
        else:
            if currentRing:
                if time.monotonic() > ringTapTime + 1:
                    print("<long pressed>")



    else:
        led.value = False






    time.sleep(0.5)
