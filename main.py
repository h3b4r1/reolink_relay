import json
import functions

# Load config
with open('config.json') as fh:
    config = json.load(fh)

# create nvr_obj
nvr_obj = functions.Reo_api()

def main(nvr_obj):
    while True:
        # defines poll interval
        sleep(config["operation"]["poll_int"])
        # Pull the API value


if __name__ == "__main__":
    main()