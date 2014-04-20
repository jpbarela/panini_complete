import random

class Pack:

    def __init__(self, pack_size, collection_size):
        self.__pack_size = pack_size
        self.__collection_size = collection_size
        self.__stickers = []
        self.__generate_pack()

    def contents(self):
        return self.__stickers

    def __generate_pack(self):
        for x in range (1,self.__pack_size+1):
            self.__add_sticker()
        self.__remove_duplicate_stickers()
        while len(self.__stickers) < self.__pack_size:
            self.__add_sticker()
            self.__remove_duplicate_stickers()
        self.__sort_stickers()
        return self.__stickers

    def __add_sticker(self):
        self.__stickers.append(random.randint(0, self.__collection_size-1))

    def __remove_duplicate_stickers(self):
        self.__stickers = list(set(self.__stickers))

    def __sort_stickers(self):
        self.__stickers.sort()