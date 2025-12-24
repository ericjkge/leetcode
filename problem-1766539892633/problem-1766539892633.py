# Last updated: 12/24/2025, 9:31:32 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = high = 0
4
5        for char in s:
6            if char == "(":
7                low += 1
8                high += 1
9            elif char == ")":
10                low -= 1
11                high -= 1
12            else:
13                low -= 1
14                high += 1
15
16            if high < 0:
17                return False
18
19            low = max(0, low)
20        
21        return low == 0
22