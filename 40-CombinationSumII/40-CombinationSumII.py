# Last updated: 1/11/2026, 10:17:13 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        n = len(candidates)
4        candidates.sort()
5        print(candidates)
6        ans = []
7
8        def backtrack(i, path):
9            if sum(path) == target:
10                ans.append(path[:])
11                return
12
13            if sum(path) > target:
14                return
15
16            for j in range(i, n):
17                if j > i and candidates[j] == candidates[j - 1]:
18                    continue
19                path.append(candidates[j])
20                backtrack(j + 1, path)
21                path.pop()
22        
23        backtrack(0, [])
24        return ans