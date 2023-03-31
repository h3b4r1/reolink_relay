import requests
import stm

class Reo_api:
    '''
    Class for accessing the reolink NVR API
    
    workflow:
    - create object with nvr ip and api key
    - provide for retreival of alarm state
    
    '''
    def __init__(self,ip,api_key):
        ''' instantiate the NVR object '''
        self.ip = ip
        self.api_key = api_key
        self.api_obj = requests(f"http://{self.ip}")
        
        @property
        def __str__(self):
            ''' return true if request object valid '''
            if self.api_obj:
                return True
            else:
                return False
            
        @property
        ''' return api key '''
        def api_key(self):
            return self._api_key
        
        @api_key.setter
        ''' set api key'''
        def api_key(self,api_key):
            if self.api_key:
                self._api_key = self.api_key
            else:
                raise ValueError("API key is required")
        
        @property
        ''' return nvr ip address '''
        def ip(self):
            return self._ip
        
        @ip.setter
        ''' set nvr ip address '''
        def ip(self,ip):
            if self.ip:
                self._ip = self.ip
            else:
                raise ValueError("IP address is required")
            
        @property
        ''' Get current alarm state '''
        def alm_state(self):
            return self.api_obj()
            ...
        
