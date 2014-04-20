from Panini import Pack

class StickerCollection:

    def __init__(self, size, stickers_requestable, pack_size):
        self.__size = size
        self.collection = [0] * size
        self.stickers = 0
        self.__threshold = size - stickers_requestable
        self.__pack_size = pack_size

    def packs_till_complete(self):
        packs = 0
        while self.stickers < self.__threshold:
            self.add_pack()
            packs += 1
        return packs

    def add_pack(self):
        new_pack = Pack.Pack(self.__pack_size, self.__size)
        for i in new_pack.contents():
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1