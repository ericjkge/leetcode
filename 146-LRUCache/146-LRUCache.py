# Last updated: 8/29/2025, 9:29:24 PM
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = self.prev =  None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node() # Left most recent
        self.left.next, self.right.prev = self.right, self.left

    def add(self, node):
        nxt = self.left.next
        self.left.next = node
        nxt.prev = node
        node.prev, node.next = self.left, nxt
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        
        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)