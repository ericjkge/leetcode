# Last updated: 6/15/2026, 7:10:01 PM
1class Solution:
2    def processStr(self, s: str) -> str:
3        res = []
4
5        for char in s:
6            if char == "*":
7                if res:
8                    res.pop()
9            elif char == "#":
10                res = res + res
11            elif char == "%":
12                res = res[::-1]
13            else:
14                res.append(char)
15
16        return "".join(res)          