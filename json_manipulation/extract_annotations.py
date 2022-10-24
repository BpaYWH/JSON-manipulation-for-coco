import os
import json

from_folder = False
number = 1

folder_path = 'C:\\Users\\user\\Desktop\\working_bench\\underwater_0901\\0521\\0521_problem'

json_path = 'C:\\Users\\user\\Desktop\\working_bench\\mpii\\mpiitrain_annotonly_test.json'

def extract_from_folder(js, fp):
    img_name = os.listdir(fp)
    images = js["images"]
    annotations = js["annotations"]
    new_images = []
    new_annotations = []
    print("No. of images: ", len(images), "No. of annotations: ", len(annotations))
    for img in img_name:
        for i in images:
            if i["file_name"] == img:
                new_images.append(i)
                break
    for n_i in new_images:
        for anot in annotations:
            if anot["image_id"] == n_i["id"]:
                new_annotations.append(anot)
    dataset = {
        "categories": js["categories"],
        "licenses": [],
        "images": new_images,
        "annotations": new_annotations
    }
    print("No. of images extracted: ", len(new_images), "No. of annotations extracted: ", len(new_annotations))
    # for a in new_annotations:
        # print(a["image_id"])
    with open(folder_path + '_selected.json', 'w') as w:
        json.dump(dataset, w)
    return

def extract_from_no(js, number):
    images = js["images"]
    annotations = js["annotations"]
    new_images = images[:number]
    new_annotations = []
    for img in new_images:
        for anot in annotations:
            if anot["image_id"] == img["id"]:
                new_annotations.append(anot)
    dataset = {
        "categories": js["categories"],
        "licenses": [],
        "images": new_images,
        "annotations": new_annotations
    }
    with open(json_path[:-5] + '_selected' + str(number) + '.json', 'w') as w:
        json.dump(dataset, w)
    print(len(new_images))
    print(len(new_annotations))
    return

with open(json_path, 'r') as r:
    js = json.loads(r.read())

if from_folder:
    extract_from_folder(js, folder_path)
else:
    extract_from_no(js, number)