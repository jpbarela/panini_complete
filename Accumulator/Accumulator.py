import math

class Accumulator:

    def __init__(self):
        self.total_packs = []
        self.total_of_squares_packs = 0
        self.count_packs = 0

        self.total_stickers = []
        self.total_of_squares_stickers = 0
        self.count_stickers = 0

    def add_value_packs(self, value):
        self.count_packs += 1
        self.total_packs.append(value)
        self.total_of_squares_packs += value ** 2

    def add_value_stickers(self, value):
        self.count_stickers += 1
        self.total_stickers.append(value)
        self.total_of_squares_stickers += value ** 2


    def average_packs(self):
        return sum(self.total_packs) / self.count_packs

    def min_packs(self):
        return min(self.total_packs)

    def max_packs(self):
        return max(self.total_packs)

    def variance_packs(self):
        print((self.total_of_squares_packs / self.count_packs) - (self.average_packs() ** 2))
        return (self.total_of_squares_packs / self.count_packs) - (self.average_packs() ** 2)

    def standard_deviation_packs(self):
        return math.sqrt(self.variance_packs())

    def average_stickers(self):
        return sum(self.total_stickers) / self.count_stickers

    def min_stickers(self):
        return min(self.total_stickers)

    def max_stickers(self):
        return max(self.total_stickers)