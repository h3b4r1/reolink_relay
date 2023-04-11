from time import sleep
from functions import Reo_api, lcd_load, lcd_create, get_api_token, alm_state, get_dev_info

# Configure the LCD 
lcd = lcd_create(0x27, 5, 4)
sleep(2)

# Configure the siren
p2 = Pin(2, Pin.OUT)

# Set up API
token = 0
while not token:
    try:
        token = get_api_key(config)
    except Exception as error:
        lcd_load(lcd, "API Failure", sta_if.ifconfig()[0])
        sleep(10)

def main():
    message = "  Boot Success"
    address = ""
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


if __name__ == "__main__":
    main()