#!/usr/local/bin/python3
import argparse
import math

import Panini
from Panini import StickerCollection
from Accumulator import Accumulator

parser = argparse.ArgumentParser('Simulate creating a Panini sticker collection')

parser.add_argument('runs', metavar='N', type= int)

runs = parser.parse_args().runs

results = Accumulator.Accumulator()
resultsSticker = Accumulator.Accumulator()

for i in range(runs):
    collection = StickerCollection.StickerCollection(Panini.NUMBER_OF_STICKERS, Panini.STICKERS_TO_REQUEST, Panini.STICKERS_PER_PACK, Panini.ALREADY_OWNED_PACKS)
    forSticker = StickerCollection.SpecificSticker(Panini.NUMBER_OF_STICKERS, Panini.STICKERS_PER_PACK)
    results.add_value(collection.packs_till_complete())
    resultsSticker.add_value(forSticker.packs_till_complete())

print("Number of runs: {0}".format(runs))
print("promedio numero de empaques para llenar el album: {0} (por un total de  {1})".format(math.ceil(results.average()),math.ceil(results.average())*18))
print("minimo numero de empaques para llenar el album: {0} (por un total de  {1})".format(results.min(),results.min()*18))
print("maximo numero de empaques para llenar el album: {0} (por un total de  {1})".format(results.max(),results.max()*18))
print("desviacion estandar de empaques para llenar el album: {0}".format(results.standard_deviation()))
print()
print("promedio numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(math.ceil(resultsSticker.average()),math.ceil(resultsSticker.average())*18))
print("minimo numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(resultsSticker.min(),resultsSticker.min()*18))
print("maximo numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(resultsSticker.max(),resultsSticker.max()*18))
print("desviacion estandar de empaques para obtener un sticker: {0}".format(resultsSticker.standard_deviation()))