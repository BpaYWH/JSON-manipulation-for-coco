## **Some python codes to handle image dataset in json format**

### Example files structure:

    |- ExampleFolder
        |- JsonFolder
            |- a.json
            |- b.json
        |- ImageFolder1
            |- 1.jpg
            ...
            |- 100.jpg
        |- ImageFolder2
            |- a1.jpg
            ...
            |- a100.jpg
            
### Action list:

#### [check_no_annotation] check (--json)

**Usage:** return how many images that are annotated

```
    Example:
        python main.py --action check --json /Example/JsonFolder/a.json 
        
    Output:
	    =========================================
	    Checking a.json ....
		=========================================
		Annotated images: 276
		Non-annotated images: 3
		Total no. of annotations: 279
		Finished checking
		
```

---

#### [listItem] list (--json)

**Usage**: return the overview of the json file

```
	Example:
        python main.py --action list --json /Example/JsonFolder/b.json

	Output:
		=========================================
		Opening b.json ....
		=========================================
		categories
		['id', 'name', 'supercategory', 'keypoints', 'keypoints_style']
		categories  count:  1
		
		licenses
		[]
		licenses  count:  0
		
		images
		['license', 'url', 'file_name', 'rights_holder', 'height', 'width', 'id']
		images  count:  279
		
		annotations
		['id', 'image_id', 'category_id', 'keypoints', 'bbox']
		annotations  count:  276
		
		Item count:  4
		Finished
```

**b.json structure**
```json
	"categories": {
		[
			"id",
			"name",
			"supercategory",
			"keypoints",
			"keypoints_style"
		]
	},
	"licenses": {},
	"images": {
		[
			"license",
			"url",
			"file_name",
			"rights_holder",
			"height",
			"width",
			"id"
		]
	},
	"annotations": {
		[
			"id",
			"image_id",
			"category_id",
			"keypoints",
			"bbox"
		]
	}
```

---

#### [train_test_split] ttsplit (--json) ([optional][default=0.2] --ratio)

**Usage**: split a json into 2 sets, split in order
Default train to test ratio: 8 : 2

```
	Example:
        For train:test = 7:3,
        python main.py --action ttsplit --json /Example/JsonFolder/a.json --ratio 0.3
        
    Result:
        |- JsonFolder
            |- a.json
            |- a_test.json (new)
            |- a_train.json (new)
            |- b.json
            
    Output:
		No. of test images:  55
		No. of train images:  224
```

---

#### [remove_no_annot] remove (--json)

**Usage**: remove all image entries that have no annotation in a json file

```
    Example:
        python main.py --action remove --json /Example/JsonFoleder/b.json
        
    Result:
    |- JsonFolder
        |- a.json
        |- b.json
        |- b_annotonly.json (new)

	Output:
		No. of images:  279 , No. of annotations:  276
```

---

#### [rename] rename (--folder) ([optional][default=''] --prefix)

**Usage**: rename images in a folder, start from 0.jpg

    Example 1:
        python main.py --action rename --folder /Example/ImageFolder1
    
    Result:
        |- ImageFolder1
            |- 0.jpg
            ...
            |- 99.jpg
    
    Example 2:
        python main.py --action rename --folder /Example/ImageFolder1 --prefix Example
    
    Result:
        |- ImageFolder1
            |- Example1.jpg (udpated)
            ...
            |- Example100.jpg (updated)

---

#### [merge_json_2] merge (--folder)

**Usage**: merge all json files present in a folder
    
    Example:
        python main.py --action merge --folder /Example/JsonFolder
        
    Result:
        |- JsonFolder
            |- a.json
            |- b.json
            |- merge.json (new)

---

#### [genjson_2] genjson2 (--folder)

**Usage**: generate json files corresponding to the images folder inside the input folder

    Example:
        python main.py --action genjson2 --folder /Example
        
    Result:
        |- Example
            |- JsonFolder
            |- ImageFolder1
            |- ImageFolder2
            |- ImageFolder1.json
            |- ImageFolder2.json

---

#### [genjson_1] genjson1 (--folder)

**Usage**: generate json file of the input dataset folder
    
    Example:
        python main.py --action genjson1 --folder /Example/ImageFolder2
    
    Result:
        |- ImageFolder2
            |- a1.jpg
            ...
            |- a100.jpg
            |- ImageFolder2.json
(X) rename after annot, rename url, json_replace, extract_annotations, extract_non_annot_images
