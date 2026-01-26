# Last updated: 1/26/2026, 1:09:37 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        subsets = []
4
5        def backtrack(index, path):
6            if index > len(nums):
7                return
8
9            subsets.append(path[:])
10
11            for i in range(index, len(nums)):
12                path.append(nums[i])
13                backtrack(i + 1, path)
14                path.pop()
15
16        backtrack(0, [])
17        return subsets