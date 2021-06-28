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

while True:

    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        x, y, z = cp.acceleration
        print((x, y, z))


        light = cp.light
        scaledlight = int(map_range(light, 0, 312, 0, 9))
        print(scaledlight)

        # how to average so when hand cover it won't trigger the light
        if light < 3:
            cp.pixels.fill(white)
            cp.pixels.brightness = 0.5
        else:
            cp.pixels.fill(dark)


        uart_server.write("{}\n".format(x, y, z))
        time.sleep(0.1)
