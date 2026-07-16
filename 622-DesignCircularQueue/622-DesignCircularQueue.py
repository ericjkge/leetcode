# Last updated: 7/16/2026, 12:20:51 AM
1class MyCircularQueue:
2
3    def __init__(self, k: int):
4        self.queue = [-1] * k
5        self.head = self.size = 0
6        self.k = k
7
8    def enQueue(self, value: int) -> bool:
9        if self.size == self.k:
10            return False
11        
12        self.queue[(self.head + self.size) % self.k] = value
13        self.size += 1
14        return True
15
16    def deQueue(self) -> bool:
17        if self.size == 0:
18            return False
19        
20        self.head = (self.head + 1) % self.k
21        self.size -= 1
22        return True
23
24    def Front(self) -> int:
25        return -1 if self.size == 0 else self.queue[self.head]
26
27    def Rear(self) -> int:
28        return -1 if self.size == 0 else self.queue[(self.head + self.size - 1) % self.k]
29
30    def isEmpty(self) -> bool:
31        return self.size == 0
32
33    def isFull(self) -> bool:
34        return self.size == self.k
35
36
37# Your MyCircularQueue object will be instantiated and called as such:
38# obj = MyCircularQueue(k)
39# param_1 = obj.enQueue(value)
40# param_2 = obj.deQueue()
41# param_3 = obj.Front()
42# param_4 = obj.Rear()
43# param_5 = obj.isEmpty()
44# param_6 = obj.isFull()