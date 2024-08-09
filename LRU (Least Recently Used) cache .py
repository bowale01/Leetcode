Here’s a detailed explanation of how to implement an LRU (Least Recently Used) cache in Python. The LRU cache uses a combination of a hash map and a doubly linked list to efficiently manage cache operations.

LRU Cache Overview
The LRU cache keeps track of the order in which items are accessed. When the cache exceeds its capacity, it evicts the least recently used item. This is achieved with:

Hash Map: For O(1) average-time complexity lookups and updates.
Doubly Linked List: For maintaining the order of items.
Implementation
Here's a Python implementation of the LRU cache:


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key to node mapping
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """Add a node right after the head."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        """Get the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Put the value into the cache."""
        if key in self.cache:
            # Update the value of the existing node and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node
            
            if len(self.cache) > self.capacity:
                # Remove the LRU item
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

# Example usage
if __name__ == "__main__":
    lru_cache = LRUCache(2)  # Create an LRU cache with capacity 2
    lru_cache.put(1, 1)      # Cache is {1=1}
    lru_cache.put(2, 2)      # Cache is {1=1, 2=2}
    print(lru_cache.get(1))  # Returns 1 and moves key 1 to the front, Cache is {2=2, 1=1}
    lru_cache.put(3, 3)      # Evicts key 2, Cache is {1=1, 3=3}
    print(lru_cache.get(2))  # Returns -1 (not found)
    lru_cache.put(4, 4)      # Evicts key 1, Cache is {3=3, 4=4}
    print(lru_cache.get(1))  # Returns -1 (not found)
    print(lru_cache.get(3))  # Returns 3
    print(lru_cache.get(4))  # Returns 4



Explanation
Node Class:

Represents each entry in the doubly linked list with key, value, prev, and next pointers.
LRUCache Class:

Initialization (__init__):
capacity: Maximum number of items the cache can hold.
cache: Hash map to store key-to-node mappings.
head and tail: Dummy nodes to simplify boundary conditions in the doubly linked list.
Private Methods:
_remove(node): Removes a node from the list.
_add(node): Adds a node right after the head.
Public Methods:
get(key): Retrieves the value for the given key, updating its position to the front of the list.
put(key, value): Adds or updates the key-value pair, moving the node to the front if it already exists. Evicts the least recently used item if the cache exceeds its capacity.
Usage Example
Add Items: lru_cache.put(1, 1) and lru_cache.put(2, 2) populate the cache.
Access Items: lru_cache.get(1) retrieves the value of key 1 and updates its position.
Eviction: Adding a new item after exceeding capacity evicts the least recently used item.
This implementation ensures efficient cache operations with O(1) time complexity for both get and put operations.

  
