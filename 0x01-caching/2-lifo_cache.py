#!/usr/bin/python3
""" Basic Cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Basic caching policy using a stack"""

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            rm_key = self.queue.pop()
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")

        for index, value in enumerate(self.queue):
            if value == key:
                self.queue.pop(index)
        self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
