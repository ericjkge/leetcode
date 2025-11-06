# Last updated: 11/6/2025, 12:45:44 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            ans.append(path[:])

            for i in range(index + 1, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(-1, [])
        return ans