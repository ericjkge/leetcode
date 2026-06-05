# Last updated: 6/4/2026, 8:56:14 PM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        return self._f(num2) - self._f(num1 - 1)
4
5    def _f(self, n: int) -> int:
6        if n < 0:
7            return 0
8        s = str(n)
9        L = len(s)
10
11        # prev_dir: 0 none/flat, 1 up, 2 down
12        @lru_cache(maxsize=None)
13        def dp(pos, prev, prev_dir, started, tight):
14            if pos == L:
15                return (1, 0)
16            hi = int(s[pos]) if tight else 9
17            cnt = tot = 0
18            for d in range(hi + 1):
19                nt = tight and (d == hi)
20                if not started:
21                    if d == 0:
22                        c, t = dp(pos + 1, 0, 0, False, nt)
23                    else:
24                        c, t = dp(pos + 1, d, 0, True, nt)
25                    cnt += c; tot += t
26                else:
27                    contrib = 0
28                    if d > prev:
29                        nd = 1
30                        if prev_dir == 2: contrib = 1   # valley at prev
31                    elif d < prev:
32                        nd = 2
33                        if prev_dir == 1: contrib = 1   # peak at prev
34                    else:
35                        nd = 0
36                    c, t = dp(pos + 1, d, nd, True, nt)
37                    cnt += c
38                    tot += t + contrib * c
39            return (cnt, tot)
40
41        return dp(0, 0, 0, False, True)[1]