#!/usr/bin/python3
""" Document """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Document"""

    def put(self, key, item):
        """Document"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Document"""
        return self.cache_data.get(key)
