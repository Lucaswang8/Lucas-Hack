# Write your code here :-)
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import analogio
import touchio
import adafruit_lis3dh
import busio

ring = touchio.TouchIn(board.A5)
pinkie = touchio.TouchIn(board.A4)
index = touchio.TouchIn(board.A1)
middle = touchio.TouchIn(board.A3)

prevPinkie = False
prevRing = False
prevMiddle = False

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

sensorMode = 0
read_time = time.monotonic()
read_int = 0.1

acc_time = time.monotonic()
acc_int = 0.03

# intiating light sensor on board
light = analogio.AnalogIn(board.A8)

# intiating accelerometer
i2c = busio.I2C(board.ACCELEROMETER_SCL,board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c,address=0x19)
x, y, z = lis3dh.acceleration

while True:
    x, y, z = lis3dh.acceleration
    #assigning variables
    indexFinger = index.value
    currentRing = ring.value
    currentPinkie = pinkie.value
    currentMiddle = middle.value
    if time.monotonic() >= read_time:
        read_time += read_int
        #sensorMode Toggle
        if currentPinkie != prevPinkie :
            prevPinkie = currentPinkie
            if currentPinkie :
                sensorMode += 1
                if sensorMode > 1:
                    sensorMode = 0


        #sensorMode is On
        if sensorMode == 1:
            led.value = True

            #read index tap values
            if indexFinger == True:
                print("<index>")

            #read Middle short / long values
            if currentMiddle != prevMiddle:
                prevMiddle = currentMiddle
                if currentMiddle:
                    middleTapTime = time.monotonic()
                else:
                    print("<midShort>")
            else:
                if currentMiddle:
                    if time.monotonic() > middleTapTime + 1:
                        print("<midLong>")

            #read ring short / long values
            if currentRing != prevRing:
                prevRing = currentRing
                if currentRing:
                    # start timer
                    ringTapTime = time.monotonic()
                    # check if it is long pressed
                else:
                    print("<ringShort>")
            else:
                if currentRing:
                    if time.monotonic() > ringTapTime + 1:
                        print("<ringLong>")




        #sensor mode off
        else:
            led.value = False

    if time.monotonic() >= accl_time:
        acc_time += accl_int
        #read accelerometer
        x, y, z = xyz_smooth(lis3dh.acceleration, (x, y, z), 0.2)
        # print((x, y, z))

        # reverse sine of threhold to rotate device 180 degrees
        if x >= 7 and ((y < th2 and y > -th2) or (z < th2 and z > -th2)):
            up_axis = "x"
            #print("X is up")
        elif x <= -7 and ((y < th2 and y > -th2) or (z < th2 and z > -th2)):
            up_axis = "-x"
            #print("-X is up")
        elif y >= 7 and ((x < th2 and x > -th2) or (z < th2 and z > -th2)):
            up_axis = "y"
            #print("Y is up")
        elif y <= -7 and ((x < th2 and x > -th2) or (z < th2 and z > -th2)):
            up_axis = "-y"
            #print("-Y is up")
        elif z >= 7 and ((x < th2 and x > -th2) or (y < th2 and y > -th2)):
            up_axis = "z"
            #print("Z is up")
        elif z <= -7 and ((x < th2 and x > -th2) or (y < th2 and y > -th2)):
            up_axis = "-z"
            #print("-Z is up")

        # print(up_axis)

        if up_axis == "x" and sensorMode == 1:
            # the hand is in the correct position to detect a swipe
            # the z axis is parallel to the direction of the swipe gesture
            #print((z,))
            # assuming there is no significant movment on the z-axis
            if m1l is False and m1r is False:
                # let's look for a movement to the left on the z-axis
                if z < -6:
                    # mark the time
                    m1t = time.monotonic()
                    m1l = True
                #look for movement on the right
                elif z > 6:
                    # mark the time
                    m1t = time.monotonic()
                    m1r = True
            else: # m1 is True:
                # we have already recorded a move to the left on z-axis
                # so let's check how much time has passsed
                tsm1 = time.monotonic() - m1t
                # print(tsm1)
                # and reset m1 to false if too much time has passed
                if tsm1 > 0.30: # lower values respond to sharper moves
                    m1l = False
                    m1r = False
                    tsm1 = 0
                    m1t = 0
                else:
                    # the time since the first move is in a good range update the data
                    # look for a second move back to the right
                    if z > 4:
                        # this second acceleration means the hand has stopped
                        swipe = True
                        tsm1 = 0
                        m1t = 0
                        m1l = False
                        m1r = False
                        print("<left>")

                    elif z < -4:
                        swipe = True
                        tsm1 = 0
                        m1t = 0
                        m1l = False
                        m1r = False
                        print("<right>")
