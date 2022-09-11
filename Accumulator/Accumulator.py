import math

class Accumulator:

    def __init__(self):
        self.total = []
        self.total_of_squares = 0
        self.count = 0

    def add_value(self, value):
        self.count += 1
        self.total.append(value)
        self.total_of_squares += value**2

    def average(self):
        return sum(self.total) / self.count

    def min(self):
        return min(self.total)

    def max(self):
        return max(self.total)

    def variance(self):
        return (self.total_of_squares / self.count) - (self.average()**2)

    def standard_deviation(self):
        return math.sqrt(self.variance())