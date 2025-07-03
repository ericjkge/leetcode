# Last updated: 7/2/2025, 11:19:32 PM
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def add(self, node):
        nxt = self.left.next
        self.left.next = node
        nxt.prev = node
        node.next, node.prev = nxt, self.left
        
    def remove(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev, prev.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)