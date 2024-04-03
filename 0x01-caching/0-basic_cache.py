#!/usr/bin/python3
"""
.0-basic_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A basic caching system that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
