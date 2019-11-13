import glob
import json
import os

glob_data = {} 
for file in glob.glob('./website-*/content/dict_pubs.json'):
    with open(file) as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            glob_data[key] = value

for websitedir in glob.glob('./website-*/'):
    with open(os.path.join(websitedir,  'content', 'all_dict_pubs.json'), 'w') as f:
        json.dump(glob_data, f, indent=4)
