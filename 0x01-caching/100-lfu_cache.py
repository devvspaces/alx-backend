#!/usr/bin/python3
""" Basic Cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Basic caching implementation using LRU policy"""

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.rank = 0
        self.queue = dict()

    def find_lru_key(self, items):
        """ Find the least recently used key
        """
        least = self.rank
        key = None
        for k, v in items.items():
            if v < least:
                key = k
                least = v
        return key

    def find_lfu_key(self):
        """ Find the least frequently used key
        """
        most = self.rank
        key = None
        for k, v in self.queue.items():
            if v[1] < most:
                key = k
                most = v[1]
        items = {}
        for k, v in self.queue.items():
            if v[1] == most:
                items[k] = v[0]
        if len(items) > 1:
            return self.find_lru_key(items)
        return key

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            rm_key = self.find_lfu_key()
            del self.cache_data[rm_key]
            del self.queue[rm_key]
            print(f"DISCARD: {rm_key}")
        value = self.queue.get(key, (0, -1))
        self.queue[key] = (self.rank, value[1] + 1)
        self.rank += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        if value:
            self.queue[key] = (self.rank, self.queue[key][1] + 1)
            self.rank += 1
        return value
