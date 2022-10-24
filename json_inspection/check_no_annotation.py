import json

# json_path = r'C:\Users\user\Desktop\working_bench\underwater_0901\0612\0612_mul\0612_underwater_mul.json'


def check(js):
    images = js["images"]
    annotations = js["annotations"]
    has_annot = False
    cnt = 0
    for img in images:
        for annot in annotations:
            if annot["image_id"] == img["id"]:
                has_annot = True
        if not has_annot:
            print(img["file_name"], ' has no annotation')
            cnt += 1
        has_annot = False
    print('Annotated images:', len(images)-cnt, )
    print('Non-annotated images:', cnt)
    print('Total no. of annotations:', len(annotations))
    print('Finished checking')

    return

def checker(path):
    print('=========================================')
    print('Checking', path.split('\\')[-1], '....')
    print('=========================================')
    with open(path, 'r') as r:
        js = json.loads(r.read())
    check(js)