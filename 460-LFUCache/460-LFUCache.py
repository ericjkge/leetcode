# Last updated: 7/30/2025, 7:20:31 PM
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LinkedList:

    def __init__(self):
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        
    def add(self, node):
        nxt = self.left.next
        self.left.next = nxt.prev = node
        node.next, node.prev = nxt, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def pop_lru(self):
        lru = self.right.prev
        self.remove(lru)
        return lru
    
    # Added is_empty function
    def is_empty(self):
        return self.left.next == self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.min_freq = 1
        self.capacity = capacity
        self.key_to_node = {} # key to (ListNode, freq)
        self.freq_to_list = {} # freq to ListNode
        
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node, freq = self.key_to_node[key]
        self.freq_to_list[freq].remove(node)
        
        # Move up min_freq if necessary
        if freq == self.min_freq and self.freq_to_list[self.min_freq].is_empty():
            self.min_freq += 1
        
        # Make node MRU
        freq += 1
        if freq not in self.freq_to_list:
            self.freq_to_list[freq] = LinkedList()
        self.freq_to_list[freq].add(node)
        
        # Update freq in key_to_node
        self.key_to_node[key] = (node, freq)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node, freq = self.key_to_node[key]
            node.val = value
            self.get(key) # Updates freq and MRU status
            return
        
        # Key not in key_to_node case
        if len(self.key_to_node) >= self.capacity:
            lfu = self.freq_to_list[self.min_freq]
            lru = lfu.pop_lru()
            del self.key_to_node[lru.key]
            
        node = ListNode(key, value)
        self.min_freq = 1
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = LinkedList()
        self.freq_to_list[1].add(node)
        self.key_to_node[key] = (node, 1)
            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)