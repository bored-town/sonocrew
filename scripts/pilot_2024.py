import json
from common import *

EVENT_NAME  = 'Pilot 2024'
INPUT_PATH  = '/Users/m1/Desktop/Export/metadata/{}.json'
OUTPUT_PATH = '../json/{}.json'
IPFS_URI    = 'ipfs://bafybeidojtfjukvxqfrde2cej4fajj7rilqmitnrxeqjtrlprpzojnozy4/{}.png'

id_mapper = [
    492, 182, 847, 55, 406, 439, 126, 945, 90, 610,     # 1-10
    19,  144, 256, 552,536, 2,   766, 3,   7,  994,     # 11-20
    86,  349, 463, 22, 4,   15,  217, 936, 159,         # 21-29
]

# check duplicate ids
dup_ids = get_duplicate_ids(id_mapper)
if (len(dup_ids) > 0):
    print("duplicated ids: {}".format(dup_ids))
    exit()

for idx, token_id in enumerate(id_mapper):
    event_id = idx + 1
    src = INPUT_PATH.format(event_id)
    dest = OUTPUT_PATH.format(token_id)

    # load json
    data = json.load(open(src))

    # update data
    data['name'] = "Sono Crew #{}".format(token_id)
    data['image'] = IPFS_URI.format(event_id)
    data['attributes'].append({'trait_type': 'Event', 'value': EVENT_NAME})

    # write file
    print(dest)
    with open(dest, "w") as f:
        json.dump(data, f)
