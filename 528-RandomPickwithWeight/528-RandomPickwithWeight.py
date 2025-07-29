# Last updated: 7/29/2025, 6:25:04 PM
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[i - 1] + w[i])

    def pickIndex(self) -> int:
        import random
        
        r = random.randint(1, self.prefix[-1])
        
        left, right = 0, len(self.prefix) - 1
        while left + 1< right:
            mid = (left + right) // 2
            if self.prefix[mid] <= r:
                left = mid
            else:
                right = mid
            
        if r <= self.prefix[left]:
            return left
        return right
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()