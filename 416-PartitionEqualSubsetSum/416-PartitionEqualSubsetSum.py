# Last updated: 7/3/2025, 4:53:26 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        @cache
        def dfs(i, curr):
            if curr == target:
                return True
            if curr > target or i == len(nums):
                return False

            return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

        return dfs(0, 0) 