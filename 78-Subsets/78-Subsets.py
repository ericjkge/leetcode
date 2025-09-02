# Last updated: 9/2/2025, 7:59:31 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(index, path):
            ans.append(path[:])

            if len(path) == n:
                return

            for i in range(index, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans