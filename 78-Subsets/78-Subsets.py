# Last updated: 11/23/2025, 11:53:59 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, index):
            if index > len(nums):
                return

            ans.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
            
        backtrack([], 0)
        return ans