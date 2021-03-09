# Design Hashmap
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3663/
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.hashmap = dict()
        self.size = 32000
        self.hashmap = [[] for x in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # self.hashmap[key] = value
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.hashmap[hash_key]):
            if k == key:
                self.hashmap[hash_key][i] = (key, value)
                return
        self.hashmap[hash_key].append((key, value))
        
    def _hash(self, key: int):
        return key*(key+3) % self.size

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # return self.hashmap.get(key, -1)
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.hashmap[hash_key]):
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # if key in self.hashmap:
        #     del self.hashmap[key]
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.hashmap[hash_key]):
            if k == key:
                self.hashmap[hash_key].remove((k,v))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)