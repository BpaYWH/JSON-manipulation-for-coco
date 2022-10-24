import glob
import os
from PIL import Image
import json


def generator(path):
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
        "id" : "0",
        "name" : "human",
        "supercategory" : "human",
        "keypoints" : keypoints,
        "keypoints_style" : keypoints_style
    }]

    dir = path + '\\'
    dataName = path.split('\\')[-1]

    image_dir_regx = dir + "*.jpg"
    images = []
    for image_path in glob.glob(image_dir_regx):
        image_file_name = os.path.basename(image_path)
        image_id = os.path.splitext(image_file_name)[0]
        image_url = "http://localhost:8007/" + image_file_name
        im = Image.open(image_path)
        width, height = im.size
        images.append({
            "id" : image_id,
            "width" : im.size[0],
            "height" : im.size[1],
            "file_name" : image_file_name,
            "url" : image_url
        })

    dataset = {
        "categories" : categories,
        "images" : images,
        "annotations" : [],
        "licenses" : []
    }

    dataset_file_path = dir + dataName + ".json"
    with open(dataset_file_path, 'w') as f:
        json.dump(dataset, f)