# Last updated: 3/21/2026, 1:42:32 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        partitions = []
4
5        def backtrack(index, path):
6            if index == len(s):
7                partitions.append(path[:])
8                return
9
10            for j in range(index + 1, len(s) + 1):
11                if s[index:j] == s[index:j][::-1]:
12                    path.append(s[index:j])
13                    backtrack(j, path)
14                    path.pop()
15        
16        backtrack(0, [])
17        return partitions