class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Call to put to handle LRU placement
            self.put(key, self.cache[key])
        # Return a default of '-1' if key does not exist
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # Remove key-value if it exists
        self.cache.pop(key, None)
         # Insert key-value at top of key stack
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Delete LRU (bottom of key stack)
            del self.cache[next(iter(self.cache))]
