import urequests
import ujson
from machine import Pin, I2C
from i2c_lcd import I2cLcd

class Reo_api:
    '''
    Class for accessing the reolink NVR API
    
    workflow:
    - create object with nvr ip and api key
    - provide for retreival of alarm state
    
    '''
    def __init__(self, config):
        ''' instantiate the NVR object '''
        self.config = config
        self.get_api_token()
    
    def alm_state(self):
        ''' get alarm state '''
        payload = ujson.dumps({"cmd":"GetMdState","action":1,"param":{"channel":0}})
        return urequests.post(f'http://{self.config["reolink"]["nvr_ip"]}/api.cgi?cmd=GetAlarm&token={self.api_token}', json=payload, timeout=5).json()
        
    def get_api_token(self):
        ''' Load api_token with a fresh token '''
        payload = ujson.dumps({"cmd":"Login","param":{"User":{"Version":"0","userName":self.config["reolink"]["nvr_un"],"password":self.config["reolink"]["nvr_pw"]}}})
        try:
            self.api_token = urequests.post(f'http://{self.config["reolink"]["nvr_ip"]}/api.cgi?cmd=Login', json=payload, timeout=5).json()[0]["value"]["Token"]["name"]
            return 0
        except EXception as e:
            raise ValueError(e)


# LCD Functions
def lcd_load(lcd, message="", address=""):
    lcd.clear()
    lcd.putstr(f"{address}" + " " * (16 - len(address)))
    if message:
        lcd.putstr(message)
    else:
        lcd.putstr("-" * 16)


def lcd_create(addr, sclPin, sdaPin):
    I2C_ADDR = addr
    totalRows = 2
    totalColumns = 16
    i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin), freq=10000)
    return I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
