# This problem was recently asked by Apple:

# LRU cache is a cache data structure that has limited space, and once there are more items in the cache than available space,
# it will preempt the least recently used item. What counts as recently used is any item a key has 'get' or 'put' called on it.

# Implement an LRU cache class with the 2 functions 'put' and 'get'. 'put' should place a value mapped to a certain key, and preempt items if needed.
# 'get' should return the value for a given key if it exists in the cache, and return None if it doesn't exist.
from datetime import datetime


class LRUCache:
    def __init__(self, space):
        # Fill this in.
        self.space = space
        # [{ key: key, value: value }]
        self.cache = []

    def get(self, key):
        # Fill this in.
        if key in [dicts["key"] for dicts in self.cache]:
            ansDict = [dicts for dicts in self.cache if dicts["key"] == key]
            val = ansDict[0]["value"]
            # rearrange
            self.cache.insert(0, self.cache.pop(self.cache.index(ansDict[0])))
            return val
        else:
            return None

    def put(self, key, value):
        # Fill this in.
        temp = {"key": key, "value": value}
        if len(self.cache) >= self.space:
            self.cache.pop()

        self.cache.append(temp)
        temp = {}


cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3
