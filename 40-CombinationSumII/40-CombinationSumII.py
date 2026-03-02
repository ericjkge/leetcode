# Last updated: 3/2/2026, 9:25:26 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        combinations = []
4        candidates.sort()
5
6        def backtrack(index, path):
7            if sum(path) == target:
8                combinations.append(path[:])
9                return
10            
11            if sum(path) > target:
12                return
13
14            for i in range(index, len(candidates)):
15                if i > index and candidates[i] == candidates[i - 1]:
16                    continue
17                path.append(candidates[i])
18                backtrack(i + 1, path)
19                path.pop()
20
21        backtrack(0, [])
22        return combinations