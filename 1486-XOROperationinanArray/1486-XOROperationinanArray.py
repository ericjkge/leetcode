# Last updated: 10/25/2025, 11:24:13 PM
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []

        for i in range(n):
            nums.append(start + 2 * i)
        
        ans = nums[0]

        for j in range(1, n):
            ans ^= nums[j]
        
        return ans