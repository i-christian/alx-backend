#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class"""

from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An implementation of LFU (Least Frequently Used) Cache Replacement Policy.

    Attributes:
        __stats (dict): Tracks the frequency of key accesses.
        __rlock (RLock): Lock accessed resources to prevent race conditions.
    """

    def __init__(self):
        """Instantiation method, initializes instance attributes."""
        super().__init__()
        self.__stats = {}
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
        Retrieves an item from the cache based on the provided key
        and updates its access frequency.

        Args:
            key: The key to identify the item.

        Returns:
            The item associated with the given key,
            or None if the key is not found.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """
        Removes the least frequently used item from the cache
        when it reaches its maximum capacity.

        Args:
            keyIn: The key of the item being added to the cache.

        Returns:
            The key of the evicted item, if any.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
