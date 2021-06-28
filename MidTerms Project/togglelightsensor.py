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

ledMode = 0
preReading = False


while True:

    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        '''
        buttonInput = cp.button_a
        if buttonInput != preReading:
            preReading = buttonInput
            if buttonInput:
                ledMode += 1
                if ledMode > 1:
                    ledMode = 0

        print(ledMode)

        if ledMode == 1:

            cp.pixels.fill(white)
            cp.pixels.brightness = 0.5
        else:
            cp.pixels.fill(dark)
        '''


        x, y, z = cp.acceleration
        # print((x, y, z))


        light = cp.light
        scaledlight = int(map_range(light, 0, 312, 0, 9))
        # print(scaledlight)

        if light < 3:

            preReading = buttonInput
            cp.pixels.fill(white)
            cp.pixels.brightness = 0.5
            if buttonInput != preReading:
                preReading = buttonInput
                if buttonInput:
                    cp.pixels.fill(dark)

        else:
            cp.pixels.fill(dark)
            if buttonInput != preReading:
                preReading = buttonInput
                if buttonInput:
                    cp.pixels.fill(white)


        uart_server.write("{}\n".format(x, y, z))
        time.sleep(0.1)
# Write your code here :-)
