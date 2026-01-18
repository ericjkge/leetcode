# Last updated: 1/18/2026, 10:50:27 AM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        n = len(candidates)
4        combinations = []
5
6        def backtrack(index, path):
7            if sum(path) == target:
8                combinations.append(path[:])
9                return
10            
11            if sum(path) > target:
12                return
13            
14            for i in range(index, n):
15                path.append(candidates[i])
16                backtrack(i, path)
17                path.pop()
18        
19        backtrack(0, [])
20        return combinations