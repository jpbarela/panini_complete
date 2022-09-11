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
    results.add_value_packs(collection.packs_till_complete())
    sticker_data = forSticker.packs_till_found()
    resultsSticker.add_value_packs(sticker_data[0])
    resultsSticker.add_value_stickers(sticker_data[1])


print("Number of runs: {0}".format(runs))
print("promedio numero de empaques para llenar el album: {0} (por un total de  {1})".format(math.ceil(results.average_packs()), math.ceil(results.average_packs()) * 18))
print("minimo numero de empaques para llenar el album: {0} (por un total de  {1})".format(results.min_packs(), results.min_packs() * 18))
print("maximo numero de empaques para llenar el album: {0} (por un total de  {1})".format(results.max_packs(), results.max_packs() * 18))
print("desviacion estandar de empaques para llenar el album: {0}".format(results.standard_deviation_packs()))
print()
print("promedio numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(math.ceil(resultsSticker.average_packs()), math.ceil(resultsSticker.average_packs()) * 18))
print("minimo numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(resultsSticker.min_packs(), resultsSticker.min_packs() * 18))
print("maximo numero de empaques para obtener un sticker: {0} (por un total de  {1})".format(resultsSticker.max_packs(), resultsSticker.max_packs() * 18))
print("desviacion estandar de empaques para obtener un sticker: {0}".format(resultsSticker.standard_deviation_packs()))
print()
print("promedio de estampa que fue el sticker: {0}".format(math.ceil(resultsSticker.average_stickers())))
print("minimo numero de estampa que fue el sticker: {0}".format(resultsSticker.min_stickers()))
print("maximo numero de estampa que fue el sticker: {0}".format(resultsSticker.max_stickers()))
