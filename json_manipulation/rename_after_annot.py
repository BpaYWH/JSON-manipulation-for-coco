import json
import os
import shutil

'''
file struct:
- root_folder
    - img.json
    - (output).json
    - backup
        - img1.jpg
        - img2.jpg
        ...
    - img_folder
        - img1.jpg
        - img2.jpg
        ...
'''

root_path = 'C:\\Users\\user\\Desktop\\working_bench\\underwater_0901\\0605'
image_folder_name = '0605_backup_extracted'
json_path = 'C:\\Users\\user\\Desktop\\working_bench\\underwater_0901\\0605\\merge.json'
output_path = json_path[:-5] + '_renamed.json'
copy_path = os.path.join(root_path, 'backup')

set_name = '30060500'

def rename_all(path, js):
    cnt = 0
    images = js["images"]
    annotatoins = js["annotations"]
    new_images = []
    new_annotations = []
    for img in os.listdir(path):
        name = set_name + str(cnt).zfill(4) + '.jpg'
        # if img[:8] != set_name:
        print(img)
        for i in images:
            if i["file_name"] == img:
                os.rename(os.path.join(path, img), os.path.join(path, name))
                for a in annotatoins:
                    if a["image_id"] == i["id"]:
                        a["image_id"] = name[:-4]
                        new_annotations.append(a)
                i["file_name"] = name
                i["url"] = "http://localhost:8007/" + name
                i["id"] = name[:-4]
                new_images.append(i)
                cnt += 1
                break

    dataset = {
        "categories": js["categories"],
        "licenses": [],
        "images": new_images,
        "annotations": new_annotations
    }
    with open(output_path, 'w') as w:
        json.dump(dataset, w)

with open(json_path, 'r') as r:
    js = json.loads(r.read())

shutil.copytree(os.path.join(root_path, image_folder_name), copy_path)

rename_all(os.path.join(root_path, image_folder_name), js)
