import json
import os

'''
file struct:
-folder_path
    - 1.json
    - 2.json
    - 3.json
    - [output_name].json
'''
output_name = 'merge'

keypoints = [
    "nose",
    "left_eye",
    "right_eye",
    "left_ear",
    "right_ear",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_wrist",
    "right_wrist",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_ankle",
    "right_ankle"
]

keypoints_style = [
    "#FF0000",
    "#FF7000",
    "#FFFF00",
    "#99FF00",
    "#00FF00",
    "#00FF99",
    "#00FFFF",
    "#0099FF",
    "#0000FF",
    "#9900FF",
    "#FF00FF",
    "#FF0099",
    "#FFAAAA",
    "#FFCCAA",
    "#FFFFAA",
    "#AAFFAA",
    "#AAFFFF"
]

categories_all = [{
    "id" : "0",
    "name" : "human",
    "supercategory" : "human",
    "keypoints" : keypoints,
    "keypoints_style" : keypoints_style
}]
images_all, annotations_all = [], []

def extract_data(js):
    image = js["images"]
    annotation = js["annotations"]
    for cnt in range(len(image)):
        for i in range(len(annotation)):
            if annotation[i]["image_id"] == image[cnt]["id"]:
                annotation[i]["image_id"] = image[cnt]["file_name"][:-4]
                annotations_all.append(annotation[i])

        image[cnt]["id"] = image[cnt]["file_name"][:-4]
        images_all.append(image[cnt])
    return

def merger(path):
    for jsonfile in os.listdir(path):
        if jsonfile[-5:] == '.json':
            print("Extracting ", jsonfile)
            with open(os.path.join(path, jsonfile), 'r') as r:
                js = json.loads(r.read())
            extract_data(js)
            print("Finished")

    data_all = {
        "categories": categories_all,
        "images": images_all,
        "annotations": annotations_all,
        "licenses": []
    }

    if images_all:
        with open(os.path.join(path, output_name + '.json'), 'w') as w:
            json.dump(data_all, w)

if __name__ == "__main__":
    folder_path = 'C:\\Users\\user\\Desktop\\working_bench\\temp'

    for jsonfile in os.listdir(folder_path):
        if jsonfile[-5:] == '.json':
            print("Extracting ", jsonfile)
            with open(os.path.join(folder_path, jsonfile), 'r') as r:
                js = json.loads(r.read())
            extract_data(js)
            print("Finished")

    data_all = {
        "categories": categories_all,
        "images": images_all,
        "annotations": annotations_all,
        "licenses": []
    }

    with open(os.path.join(folder_path, output_name + '.json'), 'w') as w:
        json.dump(data_all, w)