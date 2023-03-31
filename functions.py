import requests
import stm

class Reo_api:
    '''
    Class for accessing the reolink NVR API
    
    workflow:
    - create object with nvr ip and api key
    - provide for retreival of alarm state
    
    '''
    def __init__(self,ip,uname,pword):
        ''' instantiate the NVR object '''
        self.ip = ip
        self.api_cred = (uname,pword)
        self.api_obj = requests(f"http://{self.ip}")
        
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
        
        @api_key.setter
        def api_cred(self,api_key):
            if self.api_cred:
                self._api_cred = self.api_cred
            else:
                raise ValueError("NVR username and password are required")
        
        @property
        def ip(self):
            return self._ip
        
        @ip.setter
        def ip(self,ip):
            if self.ip:
                self._ip = self.ip
            else:
                raise ValueError("IP address is required")
            
        @property
        def alm_state(self):
            return self.api_obj()
            ...
        
