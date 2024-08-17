# main.py

import _thread
import uasyncio as asyncio
from display import LED_8SEG
from sensor import TempSensor
from networking import send_sensor_data

# Global variable for storing current temperature
current_temperature = 0


async def update_display():
    led = LED_8SEG()
    global current_temperature
    while True:
        led.write_num(current_temperature)
        await asyncio.sleep(0.001)  # Keep refreshing the display every 1 ms


def main():
    # Start the display update loop on core 1
    _thread.start_new_thread(lambda: asyncio.run(update_display()), ())

    # Start the sensor data collection and sending task on core 0
    sensor = TempSensor()
    send_sensor_data(sensor)

# Run the main function
main()
