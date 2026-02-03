# Last updated: 2/3/2026, 9:30:40 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = high = 0 # low is min possible open parentheses
4
5        for c in s:
6            if c == "(":
7                low += 1
8                high += 1
9            elif c == ")":
10                low -= 1
11                high -= 1
12            else:
13                low -= 1
14                high += 1
15
16            if high < 0:
17                return False
18            
19            low = max(low, 0)
20
21        return low == 0