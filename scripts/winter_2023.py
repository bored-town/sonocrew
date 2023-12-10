import json
from common import *

EVENT_NAME  = 'Winter 2023'
INPUT_PATH  = '/Users/m1/Desktop/Winter export/metadata/{}.json'
OUTPUT_PATH = '../json/{}.json'
IPFS_URI    = 'ipfs://bafybeigyq72oo74cwlbxszmjfjejr4pmmdccazvvvy7pougepjuu3yprqi/{}.png'

id_mapper = [
    158, 310, 264, 366, 909, 1068, 310, 1,  139, 193,   # 1-10
    613, 709, 932, 14,  105, 274,  463, 84, 256, 967,   # 11-20
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
    #data['image'] = IPFS_URI.format(event_id)
    data['attributes'].append({'trait_type': 'Event', 'value': EVENT_NAME})

    # write file
    print(dest)
    with open(dest, "w") as f:
        json.dump(data, f)
