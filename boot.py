import network
import json

# Load config
with open('config.json') as fh:
    config = json.load(fh)

constate = False
while not constate:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("config["network"]["ssid"]", "config["network"]["secret"]")
    constate = sta_if.isconnected()
