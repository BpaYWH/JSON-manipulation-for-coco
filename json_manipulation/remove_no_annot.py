import json

# json_path = 'F:\\Python\\JSON-dataset-manipulation\\json_example\\yoga_collection_event_1.json'

def remover(path):
    with open(path, 'r') as r:
        js = json.loads(r.read())

    images = js["images"]
    annotations = js["annotations"]
    new_images, new_annotations = [], []
    for img in images:
        for annot in annotations:
            if annot["image_id"] == img["id"]:
                if img not in new_images:
                    new_images.append(img)
                new_annotations.append(annot)
    dataset = {
        "categories": js["categories"],
        "licenses": [],
        "images": new_images,
        "annotations": new_annotations
    }

    print('No. of images: ', len(new_images), ', No. of annotations: ', len(new_annotations))
    with open(path[:-5] + '_annotonly.json', 'w') as w:
        json.dump(dataset, w)
    return