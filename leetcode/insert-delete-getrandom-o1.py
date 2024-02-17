class RandomizedSet:

    def __init__(self):
        self.hashSet = set()

    def insert(self, val: int) -> bool:
        if val in self.hashSet: 
            return False
        
        self.hashSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashSet: 
            self.hashSet.remove(val)
            return True
        return False 
        
        
    def getRandom(self) -> int:
        return random.choice(list(self.hashSet))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()