import json
import os

json_folder = ''
json_name = ''

json_path = os.path.join(json_folder, json_name)

def rename_url(js):
    images = js['images']
    new_images = []

    for img in images:


    dataset = {
        "categories": js["categories"],
        "licenses": [],
        "images": new_images,
        "annotations": js['annotations']
    }

    with open(json_path[:-5] + 'urled.json', 'w') as w:
        json.dump(dataset, w)
    return

with open(json_path, 'r') as r:
    js = json.loads(r.read())

rename_url(js)