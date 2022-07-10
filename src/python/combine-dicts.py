#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile, join
import json

DIRPATH = sys.argv[1]

all_json_files = [join(DIRPATH,f) for f in listdir(DIRPATH)  if isfile(join(DIRPATH, f))]

full_dic = {}
for a in all_json_files:
    with open(a, 'r') as f:
        dic = json.load(f)
    full_dic.update(dic)

with open("all_dates_dict.json", "w") as f:
    f.write(json.dumps(full_dic))

# print(all_json_files)
