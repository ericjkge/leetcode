# Last updated: 7/4/2026, 2:44:40 PM
1class Solution:
2    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
3        mapping = defaultdict(list)
4        res = []
5
6        for i in range(len(nums)):
7            for j in range(len(nums[i])):
8                mapping[i + j].append(nums[i][j])
9        
10        for lst in mapping.values():
11            res.extend(lst[::-1])
12
13        return res