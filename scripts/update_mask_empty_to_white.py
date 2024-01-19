import json
from pprint import pprint as pp

JSON_PATH = '../json/{}.json'

for token_id in range(1, 1_111+1):
    src = JSON_PATH.format(token_id)

    # load json
    data = json.load(open(src))
    attrs = data['attributes']

    # scan traits
    for info in attrs:
        tt = info['trait_type']
        tv = info['value']

        # find empty mask
        if (tt == 'Mask') and (tv == 'Empty'):

            # change to white
            info['value'] = 'White'

            # write file
            print(src)
            with open(src, "w") as f:
                json.dump(data, f)

            break
