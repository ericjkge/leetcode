# Last updated: 1/30/2026, 9:47:36 AM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        n = len(s)
4        partitions = []
5
6        def backtrack(index, path):
7            if index == n:
8                partitions.append(path[:])
9                return
10            
11            for i in range(index + 1, len(s) + 1):
12                substring = s[index:i]
13                if substring == substring[::-1]:
14                    path.append(substring)
15                    backtrack(i, path)
16                    path.pop()
17            
18        backtrack(0, [])
19        return partitions