# Last updated: 10/22/2025, 10:02:00 AM
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])        

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])

        def binSearch(target):
            left, right = 0, len(self.prefix) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if self.prefix[mid] <= target:
                    left = mid
                else:
                    right = mid
            if self.prefix[left] >= target:
                return left
            return right

        return binSearch(target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()