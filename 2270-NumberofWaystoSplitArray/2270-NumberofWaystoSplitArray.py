# Last updated: 10/26/2025, 10:27:05 AM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = ans = 0

        for i in range(len(nums) - 1):
            prefix += nums[i]
            if prefix * 2 >= total:
                ans += 1
        
        return ans