# Last updated: 5/18/2026, 3:37:18 PM
1class ListNode:
2    def __init__(self, key=None, val=None):
3        self.key = key
4        self.val = val
5        self.next = None
6        self.prev = None
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.dict = {}
12        self.capacity = capacity
13        self.left, self.right = ListNode(), ListNode()
14        self.left.next, self.right.prev = self.right, self.left
15
16    def add(self, node):
17        nxt = self.left.next
18        self.left.next = node
19        node.next, node.prev = nxt, self.left
20        nxt.prev = node
21
22    def remove(self, node):
23        p, n = node.prev, node.next
24        p.next, n.prev = n, p
25        
26    def get(self, key: int) -> int:
27        if key not in self.dict:
28            return -1
29        
30        node = self.dict[key]
31        self.remove(node)
32        self.add(node)
33        return node.val
34
35    def put(self, key: int, value: int) -> None:
36        if key in self.dict:
37            node = self.dict[key]
38            node.val = value
39            self.remove(node)
40            self.add(node)
41        else:
42            self.dict[key] = ListNode(key, value)
43            node = self.dict[key]
44            self.add(node)
45
46            if len(self.dict) > self.capacity:
47                lru = self.right.prev
48                self.remove(lru)
49                del self.dict[lru.key]
50
51# Your LRUCache object will be instantiated and called as such:
52# obj = LRUCache(capacity)
53# param_1 = obj.get(key)
54# obj.put(key,value)