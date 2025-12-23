# Last updated: 12/23/2025, 1:58:34 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if not self.min or val <= self.min[-1]:
10            self.min.append(val)
11
12    def pop(self) -> None:
13        val = self.stack.pop()
14        if val == self.min[-1]:
15            self.min.pop()
16
17    def top(self) -> int:
18        return self.stack[-1]
19
20    def getMin(self) -> int:
21        return self.min[-1]
22        
23
24
25# Your MinStack object will be instantiated and called as such:
26# obj = MinStack()
27# obj.push(val)
28# obj.pop()
29# param_3 = obj.top()
30# param_4 = obj.getMin()