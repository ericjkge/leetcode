# Last updated: 6/27/2025, 7:29:59 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helper or val <= self.helper[-1]:
            self.helper.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.helper[-1]:
            self.helper.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()