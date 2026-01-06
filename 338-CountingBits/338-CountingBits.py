# Last updated: 1/6/2026, 10:10:09 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4
5        for i in range(n + 1):
6            counter = 0
7            while i:
8                counter += i & 1
9                i >>= 1
10            ans.append(counter)
11        
12        return ans