import Panini
import random

def generate_pack():
    stickers = []
    for x in range (1,Panini.STICKERS_PER_PACK+1):
        stickers.append(random.randint(0, Panini.NUMBER_OF_STICKERS))
    contents = list(set(stickers))
    while len(contents) < Panini.STICKERS_PER_PACK:
        stickers.append(random.randint(0, Panini.NUMBER_OF_STICKERS))
        contents = list(set(stickers))
    contents.sort()
    return contents