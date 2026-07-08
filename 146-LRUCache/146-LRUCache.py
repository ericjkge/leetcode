# Last updated: 7/8/2026, 10:55:56 AM
1class ListNode:
2    def __init__(self, key=None, value=None):
3        self.key = key
4        self.value = value
5
6class LRUCache:
7
8    def __init__(self, capacity: int):
9        self.dict = {}
10        self.capacity = capacity
11        self.left, self.right = ListNode(), ListNode()
12        self.left.next, self.right.prev = self.right, self.left
13
14    def add(self, node):
15        nxt = self.left.next
16        self.left.next, nxt.prev = node, node
17        node.next, node.prev = nxt, self.left
18
19    def remove(self, node):
20        prv, nxt = node.prev, node.next
21        prv.next, nxt.prev = nxt, prv
22
23    def get(self, key: int) -> int:
24        if key in self.dict:
25            node = self.dict[key]
26            self.remove(node)
27            self.add(node)
28            return node.value
29        return -1
30
31    def put(self, key: int, value: int) -> None:
32        if key in self.dict:
33            node = self.dict[key]
34            node.value = value
35            self.remove(node)
36            self.add(node)
37        else:
38            new = ListNode(key, value)
39            self.dict[key] = new
40            self.add(new)
41
42            if len(self.dict) > self.capacity:
43                lru = self.right.prev
44                del self.dict[lru.key]
45                self.remove(lru)
46
47# Your LRUCache object will be instantiated and called as such:
48# obj = LRUCache(capacity)
49# param_1 = obj.get(key)
50# obj.put(key,value)