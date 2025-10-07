#  this is from a youtube video called 'Mock google coding interview with a Meta intern'

# Design a class
# 1. Inserting a value (no duplicates)
# 2. Removing a value
# 3. GetRandom a value that is already inserted (with equal probability)
# A . random.choice(list)
import random

class Store:
    def __init__(self):
        # define a hashmap and a values list
        self.values = []
        self.map = {} # store the index of the values

    def insert(self, value):
        if value in self.map:
            return
        self.values.append(value)
        self.map[value] = len(self.values) -1

    def remove(self, value):
        if value not in self.map:
            return
        index = self.map[value]
        # swapping
        last_val = self.values[-1]
        self.values[-1] = value
        self.map[last_val] = index
        self.values.pop() 
        del self.map[value]

    def get_random(self):
        return random.choice(self.values)