# Last updated: 5/3/2026, 10:51:39 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = [0] * (n + 1)
4
5        for i in range(n + 1):
6            index = i
7            count = 0
8            while i:
9                count += i & 1
10                i >>= 1
11            ans[index] = count
12        
13        return ans