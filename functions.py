import urequests
from machine import Pin, I2C
from i2c_lcd import I2cLcd


class Reo_api:
    _ipAddr = ""
    '''
    Class for accessing the reolink NVR API
    
    workflow:
    - create object with nvr ip and api key
    - provide for retreival of alarm state
    
    '''
    def __init__(self, config, ipAddr):
        ''' instantiate the NVR object '''
        self.ipAddr = ipAddr
        self.config = config
        self.api_cred = (config["reolink"]["nvr_un"],config["reolink"]["nvr_pw"])
        self._api_token = self.get_api_token(config)
        
    @property
    def __str__(self):
        ''' return true if request object valid '''
        if self.api_obj:
            return True
        else:
            return False
        
    @property
    def api_cred(self):
        return self._api_cred
    
    @api_cred.setter
    def api_cred(self,credTup):
        if credTup:
            self._api_cred = credTup
        else:
            raise ValueError("NVR username and password are required")
    
    @property
    def ip(self):
        return self._ipAddr
    
    @ip.setter
    def ip(self,ipAddr):
        if self.ipAddr:
            self._ipAddr = ipAddr
        else:
            raise ValueError("IP address is required")
        
    def alm_state(self):
        payload = '[{"cmd":"GetAlarm", "action": 1, "param":{"Alarm": {"type": "md", "channel": 0}}}]'
        return urequests.post(f'http://{self.ip}/api.cgi?cmd=GetAlarm&token={self.api_token}', json=payload).json()
        
    def get_api_token(self):
        payload = '[{"cmd":"Login", "param": {"User":{"Version":"0", "userName": self.api_cred[0], "password": self.api_cred[1]}}}]'
        return urequests.post(f'http://{self.ip}/api.cgi?cmd=Login', json=payload).json()[0]["value"]["Token"]["name"]
    

    def alm_state(config,token):
        return urequests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=GetMdState&token={token}').json()[0]["value"]["state"]

    def get_dev_info(self,config):
        payload = [
            {
                "cmd":"GetChannelStatus",
            }
        ]
        return urequests.post(f'http://{config["reolink"]["nvr_ip"]}/api.cgi?cmd=GetChannelStatus&token={self.api_token}', json=payload).json()

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
