import math

class Accumulator:

    def __init__(self):
        self.total = 0
        self.total_of_squares = 0
        self.count = 0

    def add_value(self, value):
        self.count += 1
        self.total += value
        self.total_of_squares += value**2

    def average(self):
        return self.total / self.count

    def variance(self):
        return (self.total_of_squares / self.count) - (self.average()**2)

    def standard_deviation(self):
        return math.sqrt(self.variance())