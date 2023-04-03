import json
import requests
from time import sleep

with open('config.json.local') as fh:
    config = json.load(fh)
    

def main():
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