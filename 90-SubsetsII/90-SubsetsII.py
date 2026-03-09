# Last updated: 3/9/2026, 1:34:50 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        ans = []
5
6        def backtrack(index, path):
7            ans.append(path[:])
8
9            for i in range(index, len(nums)):
10                if i > index and nums[i] == nums[i - 1]:
11                    continue
12                path.append(nums[i])
13                backtrack(i + 1, path)
14                path.pop()
15            
16        backtrack(0, [])
17        return ans
18