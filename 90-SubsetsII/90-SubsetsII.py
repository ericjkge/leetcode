# Last updated: 1/27/2026, 11:33:52 AM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        subsets = []
5
6        def backtrack(index, path):
7            if index == len(nums) + 1:
8                return
9
10            subsets.append(path[:])
11
12            for i in range(index, len(nums)):
13                if i > index and nums[i] == nums[i - 1]:
14                    continue
15                path.append(nums[i])
16                backtrack(i + 1, path)
17                path.pop()
18            
19        backtrack(0, [])
20        return subsets
21
22