# Last updated: 1/19/2026, 1:08:00 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        permutations = []
4
5        def backtrack(path):
6            if len(path) == len(nums):
7                permutations.append(path[:])
8                return
9            
10            for num in nums:
11                if num not in path:
12                    path.append(num)
13                    backtrack(path)
14                    path.pop()
15            
16        backtrack([])
17        return permutations