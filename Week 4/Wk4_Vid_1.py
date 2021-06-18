import board
import analogio
import time
from digitalio import DigitalInOut, Direction

# declare analog input object
analog_in = analogio.AnalogIn(board.A6)

# create a pwmout object
redled = DigitalInOut(board.A1)
redled.direction = Direction.OUTPUT
greenled = DigitalInOut(board.A2)
greenled.direction = Direction.OUTPUT
greenled2 = DigitalInOut(board.A3)
greenled2.direction = Direction.OUTPUT
yellowled = DigitalInOut(board.A4)
yellowled.direction = Direction.OUTPUT
yellowled2 = DigitalInOut(board.A5)
yellowled2.direction = Direction.OUTPUT

# declare threshold constants
TH1 = 5000
TH2 = 17000
TH3 = 29000
TH4 = 41000
TH5 = 53000

# repeat this code forever

while True :

    # gather input
    reading = analog_in.value

    # print output
    print((reading, TH1, TH2, TH3, TH4, TH5))

    # check the thresholds
    if reading > TH5:
        redled.value = True
        greenled.value = True
        greenled2.value = True
        yellowled.value = True
        yellowled2.value = True
    elif reading > TH4:
        redled.value = True
        greenled.value = True
        greenled2.value = True
        yellowled.value = True
        yellowled2.value = False
    elif reading > TH3:
        redled.value = True
        greenled.value = True
        greenled2.value = True
        yellowled.value = False
        yellowled2.value = False
    elif reading > TH2:
        redled.value = True
        greenled.value = True
        greenled2.value = False
        yellowled.value = False
        yellowled2.value = False
    elif reading > TH1:
        redled.value = True
        greenled.value = False
        greenled2.value = False
        yellowled.value = False
        yellowled2.value = False
    else:
        redled.value = False
        greenled.value = False
        greenled2.value = False
        yellowled.value = False
        yellowled2.value = False
    # sleep to prevent buffer overrun
    time.sleep(0.1)
