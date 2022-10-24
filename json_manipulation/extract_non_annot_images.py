import json
import os
import shutil

folder_path = 'C:\\Users\\user\\Desktop\\working_bench\\underwater_0901\\0605\\0605_annotated'
json_path = 'C:\\Users\\user\\Desktop\\working_bench\\underwater_0901\\0605\\0605_annotated_selected.json'

output_path = folder_path + '_extracted'
remain_path = folder_path + '_left'

if not os.path.isdir(output_path):
    os.makedirs(output_path)
if not os.path.isdir(remain_path):
    os.makedirs(remain_path)

def get_non_annot(js, fp):
    annotations = js["annotations"]
    images = js["images"]
    has_annot = False
    new_images = []
    left_images = []
    print('No. of annotations: ', len(annotations))
    print('Total no. of images: ', len(images))
    if len(annotations) > 0:
        for img in images:
            for anot in annotations:
                if anot["image_id"] == img["id"]:
                    has_annot = True

            if not has_annot:
                new_images.append(img)
            else:
                left_images.append(img)
            has_annot = False
    else:
        new_images = images

    print('Non-annotated images no.: ', len(new_images))

    for nimg in new_images:
        shutil.copyfile(os.path.join(folder_path, nimg["file_name"]), os.path.join(remain_path, nimg["file_name"]))
    for limg in left_images:
        shutil.copyfile(os.path.join(folder_path, limg["file_name"]), os.path.join(output_path, limg["file_name"]))

with open(json_path, 'r') as r:
    js = json.loads(r.read())
get_non_annot(js, folder_path)
