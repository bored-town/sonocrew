import json
from common import *
from pprint import pprint as pp

EVENT_NAME  = 'Wonderland 2024'
OUTPUT_PATH = '../json/{}.json'
IPFS_URI    = 'ipfs://bafybeihp5rcvh63mhwn63ud4biw2h7v54umsfnub7z2laemcgm5xdvrxkm'

id_mapper = [
    158, 716, 54,  1046, 146, 452, 62, 463, 685, 731,   # 1-10
    218, 638, 157, 112,  73,  734, 940,                 # 11-17
]

# check duplicate ids
dup_ids = get_duplicate_ids(id_mapper)
if (len(dup_ids) > 0):
    print("duplicated ids: {}".format(dup_ids))
    exit()

# additional config
IMG_FILENAMES = [
    '1.png',  '2.png',  '3.png',  '4.png',  '5.png',  '6.gif',  '7.gif',  '8.png',  '9.png',  '10.png',
    '11.gif', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png',
]
CSV_PATH = '../../sonocrew-assets/wonderland2024/wonderland2024.csv'
CSV_HEADER = [ 'Body', 'Head', 'Mask', 'Mouth', 'Accessorie', 'Pet', 'Front Distance' ]
vmapper = {
    'Alice': 'Alice',
    'BlackQueen': 'Black Queen',
    'Card': 'Card',
    'Caterpillar': 'Caterpillar',
    'CheshireCat': 'Cheshire Cat',
    'DarkAlice': 'Dark Alice',
    'DarkHatter': 'Dark Hatter',
    'DarkKing': 'Dark King',
    'DarkPatternAni': 'Dark Pattern',
    'DarkQueen': 'Dark Queen',
    'Dodo': 'Dodo',
    'Furry': 'Furry',
    'KingofHeart': 'King of Heart',
    'Mouth-Sew': 'Mouth Sew',
    'QueenofHeart': 'Queen of Heart',
    'Queenofheart': 'Queen of Heart',
    'RabbitTrumpet': 'Rabbit Trumpet',
    'Redmoustache': 'Red Moustache',
    'SexyQueenofHeart': 'Sexy Queen of Heart',
    'ShortBlond': 'Short Blond',
    'Tweedledum': 'Tweedledum',
    'alice': 'Alice',
    'black_g': 'Black',
    'blackani': 'Black',
    'cat': 'Cat',
    'chopped blue': 'Chopped Blue',
    'crystal': 'Crystal',
    'darkhatter': 'Dark Hatter',
    'fish_g': 'Fish',
    'fish_m': 'Fish',
    'fujinmask': 'Fuji Mask',
    'heart': 'Heart',
    'ice-mask': 'Ice Mask',
    'icemask': 'Ice Mask',
    'jokermask': 'Joker Mask',
    'knife': 'Knife',
    'lolipop': 'Lolipop',
    'madhatter': 'Mad Hatter',
    'mask': 'Mask',
    'pink': 'Pink',
    'rabbit-teeth': 'Rabbit Teeth',
    'sexyalice': 'Sexy Alice',
    'sharp teeth': 'Sharp Teeth',
    'shy': 'Shy',
    'smile_g': 'Smile',
    'spark_m': 'Spark',
    'warm breath': 'Warm Breath',
    'whiterabbit': 'White Rabbit',
    'wooden': 'Wooden',
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
