# Last updated: 3/8/2026, 9:03:24 AM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4
5        def backtrack(index, path):
6            ans.append(path[:])
7
8            for i in range(index, len(nums)):
9                path.append(nums[i])
10                backtrack(i + 1, path)
11                path.pop()
12
13        backtrack(0, [])
14        return ans