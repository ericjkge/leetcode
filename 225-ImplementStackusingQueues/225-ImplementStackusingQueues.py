# Last updated: 7/7/2025, 12:10:46 AM
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        ans = self.q1.popleft()
        for _ in range(len(self.q2)):
            self.q1.append(self.q2.popleft())
        return ans

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()