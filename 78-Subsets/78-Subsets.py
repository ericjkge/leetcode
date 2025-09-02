# Last updated: 9/1/2025, 9:35:40 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(start, path):
            ans.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans