# Last updated: 1/18/2026, 10:58:15 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        n = len(candidates)
4        combinations = []
5        candidates.sort()
6
7        def backtrack(index, path):
8            if sum(path) == target:
9                combinations.append(path[:])
10                return
11            
12            if sum(path) > target:
13                return
14            
15            for i in range(index, n):
16                if i > index and candidates[i] == candidates[i - 1]:
17                    continue
18                path.append(candidates[i])
19                backtrack(i + 1, path)
20                path.pop()
21        
22        backtrack(0, [])
23        return combinations