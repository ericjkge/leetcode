# Last updated: 9/23/2025, 8:30:53 PM
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
            if r <= self.prefix[mid]:
                right = mid
            else:
                left = mid
        
        return left if r <= self.prefix[left] else right

# [1, 3, 7, 14]
# [1, 4, 11, 25]
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()