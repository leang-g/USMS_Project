"""Hash table implementation for search, insert, and delete operations."""


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for item_index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[item_index] = (key, value)
                return

        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)

        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for item_index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[item_index]
                return True

        return False
