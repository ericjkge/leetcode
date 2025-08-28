# Last updated: 8/28/2025, 10:49:31 AM
class Solution:
    def countBits(self, n: int) -> List[int]:
        def popcount(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        return [popcount(i) for i in range(n + 1)]