import os
import pathlib
import time
import sys
import json

stats = []

with open('stats.json', 'r') as f:
    stats = json.load(f)


res = []
name = []

dir_path = "put_your_files_here"

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path != ".empty":
            res.append(path)
            name.append(path.split(".")[0])

if len(res) == 0:
    sys.exit(0)

## build

os.chdir("./challanges")
results = {}
for i,r in  enumerate(res):
    if name[i] not in results:
        results[name[i]] = []
    entry = {}
    entry["name"] = sys.argv[1]

    before = time.perf_counter()
    status = os.system("clang++ -Wall -std=c++17 {} -o {}.out".format(r,name[i]))
    after = time.perf_counter()
    entry["build-time"] = after-before
    entry["build"] = True if status == 0 else False
    entry["elapse"] = 0
    print(f"compilation took {after-before:0.4f}")
    if status == 0:
        before = time.perf_counter()
        os.system("./{}.out".format(name[i]))
        after = time.perf_counter()
        print(f"execution took {after-before:0.4f}")
        entry["elapse"] = after-before
    else:
        entry["elapse"] = 0
    results[name[i]].append(entry)

lookup = {}
for (i,k) in enumerate(stats):
    lookup[k["id"]] = i

for (key,value) in results.items():
    if key in lookup:
        stats[lookup[key]]["results"] = stats[lookup[key]]["results"] + value
    else:
        print("Unknown Challenge")

os.chdir("../")
with open('stats.json', 'w') as f:
    json.dump(stats, f)


