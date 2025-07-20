# Last updated: 7/20/2025, 11:00:55 PM
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start, path):
            if len(path) >= 2 and path not in ans:
                ans.append(path[:])
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans