# Last updated: 6/16/2026, 8:56:39 PM
1class Solution:
2    def processStr(self, s: str, k: int) -> str:
3        n = len(s)
4        lens = [0] * n
5        cur = 0
6
7        for i in range(n):
8            if s[i] == "*":
9                if cur:
10                    cur -= 1
11            elif s[i] == "#":
12                cur *= 2
13            elif s[i] == "%":
14                pass
15            else:
16                cur += 1
17            lens[i] = cur
18        
19        if k + 1 > lens[n - 1]:
20            return "."
21        
22        for i in range(n - 1, -1 , -1):
23            before = lens[i - 1] if i else 0
24            if s[i] == "*":
25                continue
26            elif s[i] == "#":
27                if k >= before:
28                    k -= before
29            elif s[i] == "%":
30                k = lens[i] - 1 - k
31            else:
32                if k == before:
33                    return s[i]
34        
35        return "."
36        
37
38            