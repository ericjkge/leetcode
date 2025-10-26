# Last updated: 10/26/2025, 10:26:03 AM
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        
        for i in range(n):
            ans ^= start + 2 * i
        
        return ans