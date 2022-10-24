import json

'''
Directly read single json file
'''

json_path = 'C:\\Users\\user\\Desktop\\annotation_use\\data\\working_bench\\test.json'
output_path = json_path[:-5] + '_replaced.json'
replace_no = 7

def rename(js):
    images = js["images"]
    annotations = js["annotations"]
    for img in images:
        if int(img["file_name"][:-4]) < replace_no:
            img["file_name"] = '0' + img["file_name"]
            img["url"] = "http://localhost:8007/" + img["file_name"]
    # for anot in annotations:
    #     if int(anot["image_id"]) < replace_no:
    #         anot["image_id"] = '0' + anot["image_id"]
    dataset = {
        "categories": js["categories"],
        "licenses": js["licenses"],
        "images": images,
        "annotations": annotations
    }
    with open(output_path, 'w') as w:
        json.dump(dataset, w)
    return

with open(json_path, 'r') as r:
    js = json.loads(r.read())
rename(js)