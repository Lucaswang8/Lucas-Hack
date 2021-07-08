# Write your code here :-)
import time
import board
import analogio
from simpleio import map_range
import neopixel
from adafruit_circuitplayground import cp

white = (255, 255, 255)
dark = (0,0,0)

preReading = False

button_pressed = False
ledState = False

accl_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

avg_accl = 0
accl_th = 20

ledState = False
movement = False
timeOut = time.monotonic()

accl_time = time.monotonic()
accl_int = 1

button_time = time.monotonic()
button_int = 0.1

timeInterval = 1

while True:

    # gather input from button and acceleration
    buttonInput = cp.button_a

    if time.monotonic() >= button_time:
        button_time += button_int
        print("reading the button")
        # check for change in the button value
        if buttonInput != preReading:
            preReading = buttonInput
            if buttonInput:
                button_pressed = True

    if time.monotonic() >= accl_time:
        # resets the next time to read the accelerometer
        accl_time += accl_int
        print("reading the accelerometer...")
        # use time.monotonic to decide when to get input/sec and average after
        x, y, z = cp.acceleration
        accl = (x, y, z)
        # print((x, y, z))
        # add all abs value of xyz values
        total_accl = 0
        for a in accl:
            total_accl += abs(a)

        # Append the new value pop an old value
        accl_vals.append(total_accl)
        accl_vals.pop(0)

        # calculate the mean
        avg_accl = sum(accl_vals)/len(accl_vals)
        print((avg_accl,))

        # is the avg_accl > threshold?
        if avg_accl >= accl_th:
            movement = True
        else:
            movement = False


    # depending on the amount of movement or the button state set the ledstate
    # print(movement)
    if movement:
        ledState = True
        # log my current time for my timeout timer
        # startTime = time.monotonic()
        # give my timeOut a time value
        timeOut = time.monotonic() + timeInterval
        button_pressed = False
    else:
        # start the timeOut timer
        # timeOut += timeInterval
        # uart_server.write("{},{}\n".format(timeOut, movement))
        # check how much time has passed
        # timePassed = timeOut - startTime
        # if timePassed >= 10:
        #     ledState = False
        if time.monotonic() == timeOut:
            ledState = False

    if button_pressed:
        ledState = not ledState
        if ledState:
            timeOut = time.monotonic() + timeInterval
        button_pressed = False
        accl_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        avg_accl = 0

    # DO THE OUTPUT BASED ON LedState
    if ledState:
        cp.pixels.fill(white)
        cp.pixels.brightness = 0.5
    else:
        cp.pixels.fill(dark)

    # this is why it is not working...
    # time.sleep(1)
# Write your code here :-)
