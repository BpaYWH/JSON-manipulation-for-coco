import os


def renamer(path, prefix):
    for i, filename in enumerate(os.listdir(path)):
        offset = 0
        while (os.path.isfile(path + '/' + prefix + str(i + offset) + ".jpg")):
            offset += 1
        if prefix in filename[:-4]:
            try:
                fileInt = int(filename[:-4])
                if fileInt <= i + offset:
                    continue
            except ValueError:
                pass
        os.rename(path + '/' + filename, path + '/' + prefix + str(i + offset) + ".jpg")

