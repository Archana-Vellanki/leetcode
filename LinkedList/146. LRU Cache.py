# 146. LRU Cache
# Solved
# Medium
# Topics
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# Time Complexity: O(1) 
# Space Complexity: O(1)

# Approach:
# In order to get O(1) complexity for get operation, we need a hashmap with key value pairs
# In order to get O(1) complexity for put operation, a doubly linkedlist would be the appropriate data structure 

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.least = Node(None, None)
        self.most = Node(None, None)
        self.least.next = self.most
        self.most.prev = self.least

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prevNode = self.most.prev
        prevNode.next = node
        node.prev = prevNode
        self.most.prev = node
        node.next = self.most

    def get(self, key: int) -> int:
        # print("get key:", key, "hashmap: ", self.hashmap)
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        # print("\n\nput key:", key, "hashmap: ", self.hashmap)
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            self.hashmap[key] = node
        else:
            newNode = Node(key, value)
            self.insert(newNode)
            self.hashmap[key] =  newNode

            if len(self.hashmap) > self.capacity:
                # evict the least recently used.
                Lru_node = self.least.next
                self.remove(Lru_node)
                del self.hashmap[Lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
