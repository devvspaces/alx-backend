#!/usr/bin/python3
""" Basic Cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Basic caching implementation using MRU policy"""

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.rank = 0
        self.queue = dict()

    def find_mru_key(self):
        """ Find the most recently used key
        """
        most = 0
        key = None
        for k, v in self.queue.items():
            if v > most:
                key = k
                most = v
        return key

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            rm_key = self.find_mru_key()
            del self.cache_data[rm_key]
            del self.queue[rm_key]
            print(f"DISCARD: {rm_key}")

        self.queue[key] = self.rank
        self.rank += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        if value:
            self.queue[key] = self.rank
            self.rank += 1
        return value
