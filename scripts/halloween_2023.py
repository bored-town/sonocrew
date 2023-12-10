import json
from common import *

INPUT_PATH  = "/Users/m1/Desktop/Export/metadata/{}.json"
OUTPUT_PATH = "../json/{}.json"
IPFS_URI    = "ipfs://bafybeicemksirajiujqwe2aatt3zzl5tlnwgv6r2vamgpadwokcz2cs5re/{}.png"

id_mapper = [
    255, 251, 214, 774, 777, 93,  135, 473,  72,   23,  # 1-10
    201, 896, 908, 122, 749, 771, 392, 1094, 1093, 272, # 11-20
    967, 102, 114, 66,  13,  229, 69,  1016, 370,  485, # 21-30
]

# check duplicate ids
dup_ids = get_duplicate_ids(id_mapper)
if (len(dup_ids) > 0):
    print("duplicated ids: {}".format(dup_ids))
    exit()

for idx, token_id in enumerate(id_mapper):
    halloween_id = idx + 1
    src = INPUT_PATH.format(halloween_id)
    dest = OUTPUT_PATH.format(token_id)

    # load json
    data = json.load(open(src))

    # update data
    data['name'] = "Sono Crew #{}".format(token_id)
    data['image'] = IPFS_URI.format(halloween_id)
    data['attributes'].append({'trait_type': 'Event', 'value': 'Halloween 2023'})

    # write file
    print(dest)
    with open(dest, "w") as f:
        json.dump(data, f)
