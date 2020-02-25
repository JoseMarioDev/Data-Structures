from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.count = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            current = self.storage[key]
            self.dll.move_to_end(current)
            return current.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        if key in self.storage:

            current = self.storage[key]
            current.value = (key, value)

            self.dll.move_to_end(current)
            return

        elif self.count < self.limit:

            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail

            self.count += 1
            
        elif self.count >= self.limit:
            
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_head()
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
