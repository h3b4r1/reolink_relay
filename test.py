import json

with open('config.json') as fh:
    config = json.load(fh)
    print(config)

print('-'*20)
print(config["operation"]["poll_int"])