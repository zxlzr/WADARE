import json
config_file = open("source_data/config")
config = json.loads(config_file.read())
c = len(config['relation2id'])
print(c)