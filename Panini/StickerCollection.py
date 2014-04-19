import Panini
from Panini import Pack

class StickerCollection:

    def __init__(self, size, stickers_requestable, pack_size):
        self.size = size
        self.collection = [0] * size
        self.stickers = 0
        self.threshold = size - stickers_requestable
        self.pack_size = pack_size

    def add_pack(self):
        new_pack = Pack.generate_pack(self.pack_size, self.size)
        for i in new_pack:
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1

    def packs_till_complete(self):
        packs = 0
        while self.stickers < self.threshold:
            self.add_pack()
            packs += 1
        return packs

