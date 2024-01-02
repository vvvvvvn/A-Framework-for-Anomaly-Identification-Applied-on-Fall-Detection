#!/usr/bin/env python
import glob
import os

import numpy as np

from processor import demo


def get_all_videos(path):
    files = [f for f in glob.glob(path + "/**/*.mp4", recursive=True)]

    return files


db = "UrFall"
path_db = "Data"
path_save = os.path.join("Myfeatures", db)

ur_adls = os.path.join(path_db, "ADLs")
print(f"ADLs: {ur_adls}")

classes = os.listdir(ur_adls)
classes.sort()


files = get_all_videos(path_db)
files.sort()

print(files)
# files.pop(0)

d = demo.Demo()
np_db = []
n_features = 256
for i, file in enumerate(files):
    print(i, "de", len(files))

    tipo = classe_name = file.split("/")[-3]
    if tipo == "ADLs":
        classe_name = file.split("/")[-2]
        index = np.array(classes.index(classe_name))
    else:
        index = np.array(len(classes))
    f3 = d.start(file, n_features=n_features)
    f3 = np.hstack((f3, index))
    np_db.append(f3)

np_db = np.array(np_db)
np.save(path_save + str(n_features) + "full", np_db)
