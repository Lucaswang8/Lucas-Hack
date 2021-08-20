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
