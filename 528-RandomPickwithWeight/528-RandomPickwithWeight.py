# Last updated: 9/23/2025, 8:23:32 PM
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])
        
    def pickIndex(self) -> int:
        import random

        r = random.randint(1, self.prefix[-1])

        left, right = 0, len(self.prefix) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix[mid] <= r:
                left = mid
            else:
                right = mid
        
        return left if r <= self.prefix[left] else right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()