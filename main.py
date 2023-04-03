import json
import functions
from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep

# Load config
with open('config.json') as fh:
    config = json.load(fh)
    
# Configure the LCD 
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
sleep(2)

# Load IP to the LCD
ifconfig = sta_if.ifconfig()
lcd.clear()
lcd.putstr(f"{ifconfig[0]}" + " " * (16 - len(ifconfig[0])))
lcd.putstr("| Remote Alarm |")

# Configure the alarm Pin
p2 = Pin(2, Pin.OUT)
p2.value(0)

# create nvr_obj
nvr_obj = functions.Reo_api()

def main(nvr_obj):
    token = 0
    while not token:
        try:
            token = get_api_key(config)
            print(f"new token : {token}")
        except Exception as error:
            print(f"API session limit exceeded : {error}")
            sleep(10)
    print(" ")
    while True:
        if alm_state(config, token):
            print("Alarm active")
            sleep(30)
        else:
            print(".", end="")
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
    return requests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=Login', json=payload).json()[0]["value"]["Token"]["name"]


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