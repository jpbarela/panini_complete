from Panini import Pack


class StickerCollection:

    def __init__(self, size, stickers_requestable, pack_size, already_owned):
        self.__size = size
        self.collection = [0] * (size - already_owned) + [1] * already_owned
        self.stickers = already_owned
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


class CollectionOnBudget:

    def __init__(self, size, pack_size, already_owned, money_to_spend, pack_price):
        self.__size = size
        self.collection = [0] * (size - already_owned) + [1] * already_owned
        self.stickers = already_owned
        self.spent = 0
        self.price = pack_price
        self.__threshold = money_to_spend
        self.__pack_size = pack_size

    def packs_opened(self):
        packs = 0
        while self.spent < self.__threshold and self.stickers < self.__size:
            self.spent += self.price
            self.add_pack()
            packs += 1
        return self.stickers

    def add_pack(self):
        new_pack = Pack.Pack(self.__pack_size, self.__size)
        for i in new_pack.contents():
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1


class SpecificSticker:

    def __init__(self, size, pack_size):
        self.__size = size
        self.collection = [0] * size
        self.stickers = 0
        # this is simulating the probability of getting card #10 given that the album is empty. i.e. the probability of obtaining a given card.
        self.__sticker = 10
        self.__pack_size = pack_size
        self.found = False

    def packs_till_found(self):
        packs = 0
        while not self.collection[self.__sticker]:
            self.add_pack()
            packs += 1
        return packs, self.stickers

    def add_pack(self):
        new_pack = Pack.Pack(self.__pack_size, self.__size)
        for i in new_pack.contents():
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1
