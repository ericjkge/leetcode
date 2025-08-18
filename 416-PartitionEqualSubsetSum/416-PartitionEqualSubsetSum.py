# Last updated: 8/18/2025, 11:51:28 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        n = len(nums)
        half = total // 2

        @cache
        def dp(i, j):
            if j == half:
                return True
            if i >= n or j > half:
                return False
            return dp(i + 1, j) or dp(i + 1, j + nums[i])
        
        return dp(0, 0)