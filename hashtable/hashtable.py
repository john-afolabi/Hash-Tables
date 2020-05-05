class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hval = 5381
        for c in key:
            hval = ((hval << 5) + hval) + ord(c)
        return hval & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)
        if self.storage[i] is not None:
            curr = self.storage[i]
            while curr:
                # Overwrites the value
                if curr.key == key:
                    curr.value = value
                    return
                # Adds and link new entry
                if curr.next is None:
                    curr.next = HashTableEntry(key, value)
                    return
                curr = curr.next
        # Starts a new linked list
        self.storage[i] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        if not self.storage[i]:
            print("key is not found")

        curr = self.storage[i]
        while curr:
            if curr.key == key:
                curr.value = None
                return
            curr = curr.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        if not self.storage[i]:
            return None
        curr = self.storage[i]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # self.capacity *= 2
        # newArr = [None] * self.capacity
        # for i, v in enumerate(self.storage):
        #     while i:
        #         newi = self.hash_index(v)
        #         newArr[newi] = v
        #     i += 1
        # return v


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
