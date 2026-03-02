# Last updated: 3/2/2026, 9:21:53 AM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        combinations = []
4
5        def backtrack(index, path):
6            if sum(path) == target:
7                combinations.append(path[:])
8                return
9            
10            if sum(path) > target:
11                return
12
13            for i in range(index, len(candidates)):
14                path.append(candidates[i])
15                backtrack(i, path)
16                path.pop()
17
18        backtrack(0, [])
19        return combinations