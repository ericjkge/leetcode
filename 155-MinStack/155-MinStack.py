# Last updated: 7/6/2025, 11:40:39 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helper or val <= self.helper[-1]:
            self.helper.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.helper[-1]:
            self.helper.pop()

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