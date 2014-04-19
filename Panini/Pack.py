import random

def generate_pack(pack_size, collection_size):
    stickers = []
    for x in range (1,pack_size+1):
        stickers.append(random.randint(0, collection_size))
    contents = list(set(stickers))
    while len(contents) < pack_size:
        stickers.append(random.randint(0, collection_size))
        contents = list(set(stickers))
    contents.sort()
    return contents