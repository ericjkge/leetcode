# Last updated: 1/6/2026, 10:09:32 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4
5        for i in range(n + 1):
6            counter = 0
7            while i:
8                if i & 1:
9                    counter += 1
10                i >>= 1
11            ans.append(counter)
12        
13        return ans