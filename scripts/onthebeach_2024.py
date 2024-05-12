import json
from common import *
from pprint import pprint as pp

EVENT_NAME  = 'On The Beach 2024'
OUTPUT_PATH = '../json/{}.json'
IPFS_URI    = 'ipfs://bafybeie3fmn2v3iuguoeqizzibvuhpxqoh55xlpys6kgyhyefx3gkbw5x4'

id_mapper = [
    37,  973, 844, 362, 50, 3, 463, 90, 22, 266,        # 1-10
    253, 875, 112,                                      # 11-13
]

# check duplicate ids
dup_ids = get_duplicate_ids(id_mapper)
if (len(dup_ids) > 0):
    print("duplicated ids: {}".format(dup_ids))
    exit()

# additional config
IMG_FILENAMES = [
    '1.gif',  '2.gif',  '3.png',  '4.png',  '5.png',  '6.png',  '7.png',  '8.gif',  '9.png',  '10.gif',
    '11.png', '12.gif', '13.gif',
]
CSV_PATH = '../../sonocrew-assets/onthebeach2024/src.csv'
CSV_HEADER = [ 'Body', 'Head', 'Mask', 'Mouth', 'Accessorie', 'Pet', 'Front Distance' ]
vmapper = {
    'Ani-Fish': 'Fish',
    'BlueHawaii': 'Blue Hawaii',
    'Card': 'Card',
    'Cloud-Dress': 'Cloud Dress',
    'DarkKing': 'Dark King',
    'Hawaii-Tattoo': 'Hawaii Tatto',
    'PinkHawaii': 'Pink Hawaii',
    'Pipe': 'Pipe',
    'Pirate': 'Pirate',
    'SailorHat': 'Sailor Hat',
    'Sea-Fish': 'Sea Fish',
    'SeaGull': 'Seagull',
    'Shellbikini': 'Shell Bikini',
    'Skull-bikini': 'Skull Bikini',
    'Squidhead': 'Squid Head',
    'Thaigreen': 'Thai Green',
    'beach-tank-top': 'Beach Tank Top',
    'bigbow-blue': 'Bigbow Blue',
    'black_g': 'Black',
    'blue-stripe-shirt': 'Blue Strip Shirt',
    'catear': 'Cat Ear',
    'coconut-pink': 'Coconut Pink',
    'coconuthead': 'Coconut Head',
    'crystal': 'Crystal',
    'flower': 'Flower',
    'flowerhead': 'Flower Head',
    'green tank top': 'Green Tank Top',
    'heart': 'Heart',
    'leaf_g': 'Leaf',
    'leaf_m': 'Leaf',
    'legendred': 'Legend Red',
    'leopard-bikini': 'Leopard Bikini',
    'lobster': 'Lobster',
    'mouth cover': 'Mouth Cover',
    'pink-bikini': 'Pink Bikini',
    'rainbow-curly': 'Rainbow Curly',
    'robot': 'Robot',
    'short-curly-surf': 'Short Curly Surf',
    'shy': 'Shy',
    'smile_g': 'Smile',
    'swimblueleaf': 'Swim Blue Leaf',
    'swimwarmflower': 'Swim Warm Flower',
    'zerogravity': 'Zero Gravity',
}

# craft csv to chars
raw = [ line.strip().split(',')[3:] for line in open(CSV_PATH, 'r') ][1:]
chars = []
missing = set()
for r in raw:
    o = {}
    for (i, h) in enumerate(CSV_HEADER):
        v = r[i] or None
        if (h == 'mask') and (v is None):
            v = 'white'
        if v is not None:
            new_v = vmapper.get(v)
            if new_v is not None:
                v = new_v
            else:
                missing.add(v)
        o[h] = v
    chars.append(o)

if (len(missing) > 0):
    pp(missing)
    exit()
#pp(chars)
#pp(vmapper)

for idx, token_id in enumerate(id_mapper):
    dest = OUTPUT_PATH.format(token_id)

    # load json
    data = json.load(open(dest))

    # update image
    data['image'] = "{}/{}".format(IPFS_URI, IMG_FILENAMES[idx])

    # update attributes
    data['attributes'] = [{ 'trait_type': 'Event', 'value': EVENT_NAME }]
    for (k, v) in chars[idx].items():
        if v is not None:
            data['attributes'].append({'trait_type': k, 'value': v})

    #print(dest)
    #pp(data)

    # write file
    print(dest)
    with open(dest, "w") as f:
        json.dump(data, f)
