"""Hash table implementation for search, insert, and delete operations."""


class HashTable:

    def __init__(self, initial_capacity=16, load_factor=0.75):
        """
        Initialize the hash table.

        Args:
            initial_capacity: Number of buckets (must be power of 2 for good hashing)
            load_factor: Threshold to trigger resize (default 0.75)
        """
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._buckets = [[] for _ in range(self._capacity)]  # Chaining
        self._count = 0

    # ---------- Core Hash Function ----------

    def _hash(self, key):
        """
        Compute the bucket index for a given key.

        Returns:
            int: Index between 0 and capacity-1
        """
        return hash(key) % self._capacity

    # ---------- Resizing (Maintains Performance) ----------

    def _resize(self):
        """
        Double the capacity when load factor is exceeded.
        Rehashes all existing entries.
        """
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._count = 0

        # Reinsert all existing items into the new buckets
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value  # Uses __setitem__

    # ---------- Dict-Like Interface ----------

    def __setitem__(self, key, value):
        """
        Insert or update a key-value pair.

        Usage: ht[key] = value
        Time Complexity: O(1) average
        """
        # Check load factor before insertion
        if (self._count + 1) / self._capacity > self._load_factor:
            self._resize()

        index = self._hash(key)
        bucket = self._buckets[index]

        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update
                return

        # Insert new pair
        bucket.append((key, value))
        self._count += 1

    def __getitem__(self, key):
        """
        Get value by key.

        Usage: value = ht[key]
        Raises KeyError if key not found.
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found in HashTable")

    def __delitem__(self, key):
        """
        Delete a key-value pair.

        Usage: del ht[key]
        Raises KeyError if key not found.
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return

        raise KeyError(f"Key '{key}' not found in HashTable")

    def __contains__(self, key):
        """
        Check if a key exists.

        Usage: if key in ht:
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def get(self, key, default=None):
        """
        Safe lookup: return value if found, else default.

        Usage: value = ht.get(key, "fallback")
        Time Complexity: O(1) average
        """
        try:
            return self[key]
        except KeyError:
            return default

    # ---------- Iteration and Views ----------

    def keys(self):
        """Return a list of all keys. (Dict-like)"""
        keys_list = []
        for bucket in self._buckets:
            for key, value in bucket:
                keys_list.append(key)
        return keys_list

    def values(self):
        """Return a list of all values. (Dict-like)"""
        values_list = []
        for bucket in self._buckets:
            for key, value in bucket:
                values_list.append(value)
        return values_list

    def items(self):
        """Return a list of all (key, value) tuples. (Dict-like)"""
        items_list = []
        for bucket in self._buckets:
            for key, value in bucket:
                items_list.append((key, value))
        return items_list

    # ---------- Additional Helpers ----------

    def __len__(self):
        """Return number of items. Usage: len(ht)"""
        return self._count

    def __str__(self):
        """String representation like a dict."""
        items_str = ", ".join([f"'{k}': {v}" for k, v in self.items()])
        return f"{{{items_str}}}"

    def __repr__(self):
        return self.__str__()

    def clear(self):
        """Remove all items."""
        self._buckets = [[] for _ in range(self._capacity)]
        self._count = 0