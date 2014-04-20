#!/usr/local/bin/python3
import argparse
import Panini
from Panini import StickerCollection
from Accumulator import Accumulator

parser = argparse.ArgumentParser('Simulate creating a Panini sticker collection')

parser.add_argument('runs', metavar='N', type= int)

runs = parser.parse_args().runs

results = Accumulator.Accumulator()

for i in (1, runs+1):
    collection = StickerCollection.StickerCollection(Panini.NUMBER_OF_STICKERS, Panini.STICKERS_TO_REQUEST, Panini.STICKERS_PER_PACK)
    results.add_value(collection.packs_till_complete())

print("Number of runs: {0}".format(runs))
print("Average number of packs needed: {0}".format(results.average()))
print("Standard deviation of packs: {0}".format(results.standard_deviation()))