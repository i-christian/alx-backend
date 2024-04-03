#!/usr/bin/python3
"""FIFO Cache Replacement Implementation Class"""

from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    An implementation of FIFO (First In, First Out) Cache Replacement Policy.

    Attributes:
        __keys: A list to keep track of keys in the order they were added.
        __rlock (RLock): A reentrant lock to ensure thread safety.
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
        Retrieves an item from the cache based on the provided key.

        Args:
            key: The key to identify the item.

        Returns:
            The item associated with the given key, else None.
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """
        Removes oldest item from the cache when it reaches its max capacity.

        Args:
            keyIn: The key of the item being added to the cache.

        Returns:
            The key of the evicted item, if any.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__keys:
                keysLength = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
                self.__keys.append(keyIn)
        return keyOut
