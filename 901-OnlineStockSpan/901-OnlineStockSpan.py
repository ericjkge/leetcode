# Last updated: 8/27/2026, 4:46:15 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = [] # (price, span)
5
6    def next(self, price: int) -> int:
7        span = 1
8        while self.stack and self.stack[-1][0] <= price:
9            _, new = self.stack.pop()
10            span += new
11        self.stack.append((price, span))
12        return span
13
14# Your StockSpanner object will be instantiated and called as such:
15# obj = StockSpanner()
16# param_1 = obj.next(price)