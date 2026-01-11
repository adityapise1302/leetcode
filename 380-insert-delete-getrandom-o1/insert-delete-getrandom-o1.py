import random
class RandomizedSet:

    def __init__(self):
        self.hashmap = dict()
        self.track_list = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.track_list)
            self.track_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        i = self.hashmap.pop(val)
        last_val = self.track_list.pop()
        if val != last_val:
            self.track_list[i] = last_val
            self.hashmap[last_val] = i
        return True

    def getRandom(self) -> int:
        return self.track_list[random.randint(0, len(self.track_list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()