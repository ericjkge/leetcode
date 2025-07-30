# Last updated: 7/30/2025, 5:16:37 PM
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        
    def add(self, node):
        nxt = self.left.next
        self.left.next = nxt.prev = node
        node.next, node.prev = nxt, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].val = value
        else:
            node = ListNode(key, value)
            self.add(node)
            self.cache[key] = node
            
            if len(self.cache) > self.capacity:
                lru = self.right.prev
                self.remove(lru)
                if lru.key in self.cache:
                    del self.cache[lru.key]