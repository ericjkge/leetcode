# Last updated: 3/25/2026, 11:13:55 AM
1class ListNode():
2    def __init__(self, key=0, value=0, next=None, prev=None):
3        self.key = key
4        self.value = value
5        self.next = next
6        self.prev = prev
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity = capacity
12        self.dict = {}
13        self.left, self.right = ListNode(), ListNode()
14        self.left.next = self.right
15        self.right.prev = self.left
16
17    def add(self, node):
18        nxt = self.left.next
19        self.left.next = node
20        nxt.prev = node
21        node.next, node.prev = nxt, self.left
22
23    def remove(self, node):
24        prev, nxt = node.prev, node.next
25        prev.next, nxt.prev = nxt, prev
26
27    def get(self, key: int) -> int:
28        if key in self.dict:
29            self.remove(self.dict[key])
30            self.add(self.dict[key])
31            return self.dict[key].value
32        return -1
33
34    def put(self, key: int, value: int) -> None:
35        if key in self.dict:
36            self.remove(self.dict[key])
37            self.add(self.dict[key])
38            self.dict[key].value = value
39        else:
40            self.dict[key] = ListNode(key, value)
41            self.add(self.dict[key])
42        
43        if len(self.dict) > self.capacity:
44            lru = self.right.prev
45            self.remove(lru)
46            del self.dict[lru.key]
47
48# Your LRUCache object will be instantiated and called as such:
49# obj = LRUCache(capacity)
50# param_1 = obj.get(key)
51# obj.put(key,value)