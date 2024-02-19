import json
from common import *
from pprint import pprint as pp

EVENT_NAME  = 'GAS 2024'
OUTPUT_PATH = '../json/{}.json'
IPFS_URI    = 'ipfs://bafybeieouanb6hnzoreqofdlaldpulz4sxlkd47ffzicwhoqcj2zselwou'

id_mapper = [
    4,    890, 158,  392, 532, 145, 255, 311,  282,  938, # 1-10
    1095, 231, 76,   8,   940, 536, 162, 1057, 1108, 428, # 11-20
    463,  217, 1017, 629, 198,                            # 21-25
]

# check duplicate ids
dup_ids = get_duplicate_ids(id_mapper)
if (len(dup_ids) > 0):
    print("duplicated ids: {}".format(dup_ids))
    exit()

# additional config
IMG_FILENAMES = [
    '1.png',  '2.gif',  '3.png',  '4.gif',  '5.png',  '6.gif',  '7.png',  '8.png',  '9.gif',  '10.gif',
    '11.gif', '12.png', '13.png', '14.gif', '15.png', '16.png', '17.gif', '18.png', '19.png', '20.gif',
    '21.png', '22.png', '23.png', '24.png', '25.gif',
]
CSV_PATH = '../csv/gas_2024.csv'
CSV_HEADER = [ 'Body', 'Head', 'Mask', 'Mouth', 'Accessorie', 'Pet', 'Front Distance' ]
vmapper = {
    'Bloodygal': 'Bloody Gal',
    'Darkgang': 'Dark Gang',
    'GalsGangblue': 'Gals Gang',
    'Galsgang': 'Gals Gang',
    'Goldgang': 'Gold Gang',
    'Hebigang': 'Hebi Gang',
    'Hebisnake': 'Hebi Gang',
    'Huntergang': 'Hunter Gang',
    'Machinegungang': 'Machine Gun Gang',
    'Orange': 'Orange',
    'Rozugang': 'Rozu Gang',
    'Skeletongang': 'Skeleton Gang',
    'anarchygang': 'Anarchy Gang',
    'ani-laugh': 'Laugh',
    'bear': 'Bear',
    'beatgang': 'Beat Gang',
    'biggang': 'Big Gang',
    'birdnestblue': 'Birdnestblue',
    'blackani': 'Black',
    'blackanimate': 'Black',
    'bloodgang': 'Blood Gang',
    'bushidogang': 'Bushido Gang',
    'catear': 'Catear',
    'cigarette': 'Cigarette',
    'darkgang': 'Dark Gang',
    'deathgang': 'Death Gang',
    'firegang': 'Fire Gang',
    'firemaskani': 'Fire',
    'flower': 'Flower',
    'frozen-pizza': 'Frozen Pizza',
    'fujingang': 'Fujin Gang',
    'fujinmask': 'Fujin Mask',
    'gasmask': 'GasMask',
    'ghost': 'Ghost',
    'goldgang': 'Gold Gang',
    'goldmask': 'Gold Mask',
    'green china': 'Green China',
    'grey pigtail': 'Grey Pigtail',
    'heart': 'Heart',
    'hebigang': 'Hebi Gang',
    'horror': 'Horror',
    'huntergang': 'Hunter Gang',
    'ice-mask': 'Ice Mask',
    'icemask': 'Icemask',
    'killgang': 'Kill Gang',
    'machinegungang': 'Machine Gun Gang',
    'magic-symbol': 'Magic Symbol',
    'mask': 'Mask',
    'money': 'Money',
    'monitor': 'Monitor',
    'ogre white': 'Ogre White',
    'orenge head': 'Orenge Head',
    'pierce-mouth': 'Pierce Mouth',
    'pierce-tounge': 'Pierce Tounge',
    'piggygang': 'Piggy Gang',
    'pink': 'Pink',
    'prettygang': 'Pretty Gang',
    'raijingang': 'Raijin Gang',
    'raijinmask': 'Raijin Mask',
    'sharp teeth': 'Sharp Teeth',
    'shy': 'Shy',
    'skeleton': 'Skeleton',
    'skeletongang': 'Skeleton Gang',
    'star': 'Star',
    'tattoo': 'Tattoo',
    'white': 'White',
    'white-beard': 'White Beard',
    'wooden': 'Wooden',
    'yummy': 'Yummy',
}

# craft csv to chars
raw = [ line.strip().split(',')[3:] for line in open(CSV_PATH, 'r') ][1:]
chars = []
for r in raw:
    o = {}
    for (i, h) in enumerate(CSV_HEADER):
        v = r[i] or None
        if (h == 'mask') and (v is None):
            v = 'white'
        if v is not None:
            v = vmapper[v]
        o[h] = v
    chars.append(o)

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
