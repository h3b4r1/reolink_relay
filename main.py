import json
import functions
import urequests
from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep
from functions import *

# Configure the LCD 
lcd = lcd_create(0x27, 5, 4)
sleep(2)

# Configure the siren
p2 = Pin(2, Pin.OUT)

# Set up API
token = 0
while not token:
    try:
        nvr = Reo_api(config)
    except Exception as error:
        lcd_load(lcd, "API Failure", sta_if.ifconfig()[0])
        sleep(10)

def main(nvr_obj):
    token = 0
    while not token:
        try:
            token = get_api_token(config)
            print(f"new token : {token}")
        except Exception as error:
            print(f"API session limit exceeded : {error}")
            sleep(10)
    print(" ")
    while True:
        # Load IP to the LCD
        if address != sta_if.ifconfig()[0]:
            address = sta_if.ifconfig()[0]
            lcd_load(lcd, message, address)
            sleep(2)
        
        # Pull the alarm status
        if alm_state(config, token):
            p2.value(1)
            sleep(5)
            p2.value(0)
            sleep(30)
        sleep(1)


def get_api_token(config):
    payload = [
        {
            "cmd":"Login",
            "param":{
                "User":{
                    "Version":"0",
                    "userName":config["reolink"]["nvr_un"],
                    "password":config["reolink"]["nvr_pw"]
                }
            }
        }
    ]
    return urequests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=Login', json=payload).json()[0]["value"]["Token"]["name"]


def alm_state(config,token):
    return requests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=GetMdState&token={token}').json()[0]["value"]["state"]


def get_dev_info(config,token):
    payload = [
        {
            "cmd":"GetChannelStatus",
        }
    ]
    return requests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=GetChannelStatus&token={token}', json=payload).json()


if __name__ == "__main__":
    main()