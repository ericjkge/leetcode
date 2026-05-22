# Last updated: 5/22/2026, 1:51:58 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        total = 0
4        mappings = {
5            "I": 1,
6            "V": 5,
7            "X": 10,
8            "L": 50,
9            "C": 100,
10            "D": 500,
11            "M": 1000
12        }
13
14        for i in range(len(s)):
15            if i + 1 < len(s) and mappings[s[i]] < mappings[s[i + 1]]:
16                total -= mappings[s[i]]
17            else:
18                total += mappings[s[i]]
19
20        return total
21