import ujson
from machine import Pin, I2C
# from i2c_lcd import I2cLcd
from time import sleep
from functions import *

# Configure the LCD 
lcd = lcd_create(0x27, 5, 4)
sleep(2)

# # Configure the siren
# p2 = Pin(2, Pin.OUT)

# # Load config
# with open('config.json') as fh:
#     config = ujson.load(fh)

# Set up API
nvr = 0
while not nvr:
    try:
        nvr = Reo_api(config)
    except Exception as e:
        lcd_load(lcd, "API Failure", sta_if.ifconfig()[0])
        sleep(10)

def main():
    counter = 30
    while True:
        # Get new token
        if "error" in nvr.alm_state():
            try:
                nvr.get_api_token()
            except Exception as error:
                lcd_load(lcd, "Session Lim Excd", sta_if.ifconfig()[0])
                sleep(10)
            counter = 0

        # Reload address
        if address != sta_if.ifconfig()[0]:
            address = sta_if.ifconfig()[0]
            lcd_load(lcd, message, address)
            sleep(2)

        # Pull the alarm status
        # print(f'alarm state return is: {nvr.alm_state()[0]["value"]["state"]}')
        if nvr.alm_state()[0]["value"]["state"]:
            lcd_load(lcd, "Alarm Active", sta_if.ifconfig()[0])
            p2.value(1)
            sleep(5)
            p2.value(0)
            sleep(30)
        lcd_load(lcd, "Alarm Ready", sta_if.ifconfig()[0])
        sleep(1)
        counter += 1


if __name__ == "__main__":
    main()