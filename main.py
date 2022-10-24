import argparse
from json_inspection import check_no_annotation, listItem
from json_manipulation import train_test_split, remove_no_annot, rename, genjson, genjson_2, merge_json_2

def parse_args():
    parser = argparse.ArgumentParser(description='Json dataset utilities')
    parser.add_argument('--action', '-a', required=True, type=str,
                        choices=['check', 'list', 'ttsplit', 'remove', 'rename', 'merge', 'genjson1', 'genjson2'],
                        dest='action', help='The action you would like to perform.')

    parser.add_argument('--json', '-j', required=False, type=str,
                        dest='json',
                        help='Path to the json dataset file. Required for \'check\', \'list\', \'ttslpit\', \'remove\' action.')

    parser.add_argument('--folder', '-f', required=False, type=str,
                        dest='folder',
                        help='Path to the folder, required for \'rename\', \'merge\', \'--genjson\' action.')

    parser.add_argument('--ratio', '-r', required=False, type=float, default=0.2,
                        dest='ratio',
                        help='Test-train split ratio in floating point number. Used with \'ttsplit\' action.')

    parser.add_argument('--prefix', '-p', required=False, type=str, dest='prefix', default='',
                        help='Rename prefix. Used with \'rename\' action.')

    # print(parser.parse_args())
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    action = args.action
    if action == 'check':
        if args.json is not None:
            check_no_annotation.checker(args.json)
        else:
            print("Json path is missing")

    elif action == 'list':
        if args.json is not None:
            listItem.lister(args.json)
        else:
            print("Json path is missing")

    elif action == 'ttsplit':
        if args.json is not None:
            train_test_split.splitter(args.json, args.ratio)
        else:
            print("Json path is missing")

    elif action == 'remove':
        if args.json is not None:
            remove_no_annot.remover(args.json)
        else:
            print("Json path is missing")

    elif action == 'rename':
        if args.folder is not None:
            rename.renamer(args.folder, args.prefix)
        else:
            print("Folder path is missing")

    elif action == 'genjson1':
        if args.folder is not None:
            genjson.generator(args.folder)
        else:
            print("Folder path is missing")

    elif action == 'genjson2':
        if args.folder is not None:
            genjson_2.generator(args.folder)
        else:
            print("Folder path is missing")

    elif action == 'merge':
        if args.folder is not None:
            merge_json_2.merger(args.folder)
        else:
            print("Folder path is missing")
