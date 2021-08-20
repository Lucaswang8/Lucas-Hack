import time
import board
from digitalio import DigitalInOut, Direction, Pull
import analogio
import touchio

ring = touchio.TouchIn(board.TX)
pinkie = touchio.TouchIn(board.A6)
index = touchio.TouchIn(board.A1)


while True:

    indexFinger = index.value
    ringFinger = ring.value
    pinkieFinger = pinkie.value

    if indexFinger == True:
        print("<index>")

    if ringFinger == True:
        print("<ring>")

    if pinkieFinger == True:
        print("<pinkie>")

    time.sleep(0.1)
