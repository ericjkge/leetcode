# Last updated: 5/3/2026, 10:52:19 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4
5        for i in range(n + 1):
6            count = 0
7            while i:
8                count += i & 1
9                i >>= 1
10            ans.append(count)
11        
12        return ans