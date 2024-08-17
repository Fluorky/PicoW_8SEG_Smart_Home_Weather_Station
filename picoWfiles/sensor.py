# sensor.py

from machine import ADC


class TempSensor:
    def __init__(self):
        self.sensor = ADC(4)
        self.conversion_factor = 3.3 / 65535

    def read_temp(self):
        reading = self.sensor.read_u16() * self.conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        return temperature
