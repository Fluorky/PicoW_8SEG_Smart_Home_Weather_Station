# display.py

import time
from machine import Pin, SPI

# Constants for 8-segment display
MOSI = 11
SCK = 10
RCLK = 9
THOUSANDS = 0xFE
HUNDREDS = 0xFD
TENS = 0xFB
UNITS = 0xF7
Dot = 0x80

# 7-segment display codes for numbers
SEG8Code = [
    0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D,
    0x7D, 0x07, 0x7F, 0x6F, 0x77, 0x7C,
    0x39, 0x5E, 0x79, 0x71
]


class LED_8SEG:
    def __init__(self, RCLK=RCLK, SCK=SCK, MOSI=MOSI):
        self.rclk = Pin(RCLK, Pin.OUT)
        self.rclk.value(1)
        self.spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=None)

    def write_cmd(self, num, seg):
        self.rclk.value(1)
        self.spi.write(bytearray([num, seg]))
        self.rclk.value(0)
        time.sleep(0.001)
        self.rclk.value(1)

    def write_num(self, num):
        self.write_cmd(UNITS, SEG8Code[num % 10])
        self.write_cmd(TENS, SEG8Code[(num % 100) // 10] | Dot)
        self.write_cmd(HUNDREDS, SEG8Code[(num % 1000) // 100])
        self.write_cmd(TENS, Dot)

    def clear(self):
        self.write_cmd(UNITS, 0)
        self.write_cmd(TENS, 0)
        self.write_cmd(HUNDREDS, 0)
        self.write_cmd(THOUSANDS, 0)
