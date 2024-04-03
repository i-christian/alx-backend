#!/usr/bin/python3
"""LRU Cache Replacement Implementation Class"""

from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    An implementation of LRU (Least Recently Used) Cache Replacement Policy.

    Attributes:
        __keys (list): Stores cache keys in order of recent usage.
        __rlock (RLock): Lock accessed resources to prevent race conditions.
    """

    def __init__(self):
        """Instantiation method, initializes instance attributes."""
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: The key to identify the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """
        Retrieves an item from the cache based on the provided key and updates.

        Args:
            key: The key to identify the item.

        Returns:
            The item associated with the given key,
            or None if the key is not found.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__keys:
                self._balance(key)
        return value

    def _balance(self, keyIn):
        """
        Removes the least recently used item from cache when at max capacity.

        Args:
            keyIn: The key of the item being added to the cache.

        Returns:
            The key of the evicted item, if any.
        """
        keyOut = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
            else:
                self.__keys.remove(keyIn)
            self.__keys.append(keyIn)
        return keyOut
