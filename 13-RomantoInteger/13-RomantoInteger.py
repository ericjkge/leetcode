# Last updated: 5/22/2026, 1:49:56 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        total = 0
4        i = len(s) - 1
5        mappings = {
6            "I": 1,
7            "V": 5,
8            "X": 10,
9            "L": 50,
10            "C": 100,
11            "D": 500,
12            "M": 1000
13        }
14
15        while i > -1:
16            if i - 1 >= 0 and (s[i] == "V" or s[i] == "X") and s[i - 1] == "I":
17                total += mappings[s[i]] - 1
18                i -= 2
19            elif i - 1 >= 0 and (s[i] == "L" or s[i] == "C") and s[i - 1] == "X":
20                total += mappings[s[i]] - 10
21                i -= 2
22            elif i - 1 >= 0 and (s[i] == "D" or s[i] == "M") and s[i - 1] == "C":
23                total += mappings[s[i]] - 100
24                i -= 2
25            else:
26                total += mappings[s[i]]
27                i -= 1
28        
29        return total
30