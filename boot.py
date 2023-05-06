import network
import ujson
import gc
from time import sleep
from machine import Pin

# Enable garbage collection
gc.enable()

# Configure the alarm Pin
p2 = Pin(2, Pin.OUT)
p2.value(0)

# Load config
with open('config.json') as fh:
    config = ujson.load(fh)

# Setup wifi connection
sleep(10)
constate = False
count = 0
while not constate and count < 11:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(config["network"]["ssid"], config["network"]["secret"])
    sleep(2)
    count += 1
    constate = sta_if.isconnected()
    print(".", end="")
    