import json

# json_path = 'C:\\Users\\user\\Desktop\\working_bench\\mpiitrain_annotonly.json'
# test_train_ratio = 0.1

def splitter(path, test_train_ratio):
    with open(path, 'r') as r:
        js = json.loads(r.read())

    split_cnt = 0
    images = js["images"]
    annotations = js["annotations"]
    train_images, train_annotations, test_images, test_annotations = [], [], [], []
    img_cnt = len(images)
    test_img_cnt = int(img_cnt * test_train_ratio)
    for img in images:
        for annot in annotations:
            if annot["image_id"] == img["id"]:
                if split_cnt <= test_img_cnt:
                    test_annotations.append(annot)
                else:
                    train_annotations.append(annot)
        if split_cnt <= test_img_cnt:
            test_images.append(img)
        else:
            train_images.append(img)
        split_cnt += 1
    try:
        cat = js["categories"]
    except:
        cat = []
    train_dataset = {
        "categories": cat,
        "images": train_images,
        "annotations": train_annotations
    }
    test_dataset = {
        "categories": cat,
        "images": test_images,
        "annotations": test_annotations
    }

    print("No. of test images: ", test_img_cnt)
    print("No. of train images: ", split_cnt - test_img_cnt)

    test_path = path[:-5] + '_test.json'
    train_path = path[:-5] + '_train.json'
    with open(test_path, 'w') as w_test:
        json.dump(test_dataset, w_test)
    with open(train_path, 'w') as w_train:
        json.dump(train_dataset, w_train)
    return
