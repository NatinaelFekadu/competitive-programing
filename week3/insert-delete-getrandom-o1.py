class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.values)
        self.values.append(val)           
        return True                     

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]     
        last_val = self.values[-1]           
        self.values[index] = last_val         
        self.hashmap[last_val] = index 
        self.values.pop()                     
        del self.hashmap[val]           
        return True                     

    def getRandom(self) -> int:
        
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()