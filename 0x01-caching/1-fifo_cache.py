#!/usr/bin/python3
""" Basic Cache module
"""

from queue import Queue

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Basic caching policy using a queue"""

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.queue = Queue(maxsize=BaseCaching.MAX_ITEMS)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        not_there = not self.cache_data.get(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            rm_key = self.queue.get()
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")
        if not_there:
            self.queue.put(key, False)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
