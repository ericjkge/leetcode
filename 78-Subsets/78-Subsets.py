# Last updated: 11/6/2025, 12:47:23 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            ans.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans