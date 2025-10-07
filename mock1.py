# Design a class
# 1. Inserting a value (no duplicates)
# 2. Removing a value
# 3. GetRandom a value that is already inserted (with equal probability)
# A . random.choice(list)

class Store:
    def __init__(self):
        # define a hashmap and a values list
        self.values = []
        self.map = {}
        
    def insert(self, value):
        pass
    def remove(self, value):
        pass