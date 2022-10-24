import json

# json_path = r'F:\Python\JSON-dataset-manipulation\json_example\yoga_collection_event_1.json'

itemlist = []

def listItem(js):
    itemNo = 0
    for item in js:
        itemNo += 1
        memNo = 0
        print(item)
        for mem in js[item]:
            memNo += 1
            for ele in mem:
                if ele not in itemlist:
                    itemlist.append(ele)
        print(itemlist)
        print(item, " count: ", memNo)
        print()
        itemlist.clear()
    print("Item count: ", itemNo)
    print('Finished')
    return
def lister(path):
    print('=========================================')
    print('Opening', path.split('\\')[-1], '....')
    print('=========================================')
    with open(path, 'r') as r:
        js = json.loads(r.read())
    listItem(js)