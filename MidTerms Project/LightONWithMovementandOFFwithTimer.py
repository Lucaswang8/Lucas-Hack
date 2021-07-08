# Write your code here :-)
import time
import board
import analogio
from simpleio import map_range
import neopixel
from adafruit_circuitplayground import cp
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

white = (255, 255, 255)
dark = (0,0,0)

preReading = False

button_pressed = False
ledState = False

accl_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

avg_accl = 0
accl_th = 20

movement = False

timeInterval = 1

while True:

    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:

        # gather input from button and acceleration
        buttonInput = cp.button_a
        # use time.monotonic to decide when to get input/sec and average after

        x, y, z = cp.acceleration
        accl = (x, y, z)
        # print((x, y, z))

        # check for change in the button value
        if buttonInput != preReading:
            preReading = buttonInput
            if buttonInput:
                button_pressed = not button_pressed

        # add all abs value of xyz values
        total_accl = 0
        for a in accl:
            total_accl += abs(a)

        # Append the new value pop an old value
        accl_vals.append(total_accl)
        accl_vals.pop(0)

        # calculate the mean
        avg_accl = sum(accl_vals)/len(accl_vals)
        #print(avg_accl)

        # is the avg_accl > threshold?
        if avg_accl >= accl_th:
            movement = True
        else:
            movement = False
        print(movement)


        # is the led on or off?
        if ledState:

            # check if movement is still there
            if movement is False :
                # start the timeOut timer
                timeOut += timeInterval
                uart_server.write("{},{}\n".format(timeOut, movement))

                #check how much time has passed
                timePassed = timeOut - startTime
                if timePassed >= 10:
                    ledState = False


        else:
            if button_pressed or movement:
                ledState = True
                # log my current time for my timeout timer
                startTime = time.monotonic()
                #give my timeOut a time value
                timeOut = time.monotonic() + timeInterval

            # do seomthing else because the light is already off

        if ledState:

            cp.pixels.fill(white)
            cp.pixels.brightness = 0.5

        else:
            cp.pixels.fill(dark)




        time.sleep(1)

