# Last updated: 11/24/2025, 12:34:33 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(path, index):
            if index > len(nums):
                return

            ans.append(path[:])
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                else:
                    path.append(nums[i])
                    backtrack(path, i + 1)
                    path.pop()
            
        backtrack([], 0)
        return ans