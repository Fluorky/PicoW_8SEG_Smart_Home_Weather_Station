# networking.py

import network
import urequests
import time
from config import WIFI_SSID, WIFI_PASSWORD, SERVER_URL


def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print('Connecting to WiFi...')
        time.sleep(1)
    print('Connected to WiFi:', wlan.ifconfig())


def send_sensor_data(sensor):
    connect_to_wifi()
    global current_temperature
    while True:
        temperature = sensor.read_temp()
        print(f"Temperature: {temperature}")
        current_temperature = int(temperature * 10)

        data = {'temperature': temperature}
        try:
            response = urequests.post(SERVER_URL, json=data)
            print(f"POST response: {response.status_code}")
            response.close()
        except Exception as e:
            print('Error sending data:', e)
        time.sleep(2)
