#!/usr/bin/python3
"""
.0-basic_cache.py
"""
BaseCaching = __import__('base_caching').base_caching


class BasicCache(BaseCaching):
    """ A basic caching system that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
