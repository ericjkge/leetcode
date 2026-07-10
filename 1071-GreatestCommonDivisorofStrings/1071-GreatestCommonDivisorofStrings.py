# Last updated: 7/9/2026, 9:09:26 PM
1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3        ans = ""
4
5        def canDivide(s, t):
6            if len(s) % len(t):
7                return False
8            
9            for i in range(0, len(s), len(t)):
10                if s[i:i + len(t)] != t:
11                    return False
12            
13            return True
14
15        for i in range(min(len(str1), len(str2))):
16            prefix = str1[:i + 1]
17            
18            if canDivide(str1, prefix) and canDivide(str2, prefix):
19                ans = prefix
20            
21        return ans