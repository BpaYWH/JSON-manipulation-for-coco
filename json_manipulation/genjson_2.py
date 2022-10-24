import os
from PIL import Image
import json

'''
file struct:
-folder_path
    - image_folder_1
        - image_1_1.jpg 
        - image_1_2.jpg 
    - image_folder_2
        - image_2_1.jpg
        - image_2_2.jpg
    - image_folder_3 
        - image_3_1.jpg
        - image_3_2.jpg
'''


def genjson(f_path, folder):
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
    categories = [{
        "id": "0",
        "name": "human",
        "supercategory": "human",
        "keypoints": keypoints,
        "keypoints_style": keypoints_style
    }]

    path = os.path.join(f_path, folder)
    output_path = path + '.json'
    id_cnt = 0
    images = []
    for img in os.listdir(path):
        if img[-4:] == '.jpg':
            img_path = os.path.join(path, img)

            file_name = img
            id = str(id_cnt)
            im = Image.open(img_path)
            url = "http://localhost:8007/" + file_name

            id_cnt += 1
            images.append({
                "id": id,
                "width": im.size[0],
                "height": im.size[1],
                "file_name": file_name,
                "url": url
            })

    dataset = {
        "categories": categories,
        "images": images,
        "annotations": [],
        "licenses": []
    }

    if images:
        with open(output_path, 'w') as f:
            json.dump(dataset, f)

def generator(path):
    for folder in os.listdir(path):
        genjson(path, folder)

if __name__ == "__main__":
    folder_path = 'C:\\Users\\user\\Desktop\\working_bench\\0612_sin_bench'
    for folder in os.listdir(folder_path):
        genjson(folder_path, folder)

