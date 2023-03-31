import json
import requests
import sys

# Pull the config
with open('config.json') as fh:
    config = json.load(fh)
    

# Create the api object
def main():
    # print(get_api_key(config))
    # print(json.dumps(get_dev_info(config,get_api_key(config)), indent=4))
    print(json.dumps(alm_state(config,get_api_key(config)), indent=4))


def get_api_key(config):
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