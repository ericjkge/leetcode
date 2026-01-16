# Last updated: 1/16/2026, 7:15:39 PM
1class Solution:
2    def isLongPressedName(self, name: str, typed: str) -> bool:
3        i = 0
4
5        for j in range(len(typed)):
6            if i < len(name) and name[i] == typed[j]:
7                i += 1
8            elif j > 0 and typed[j] == typed[j - 1]:
9                continue
10            else:
11                return False
12        
13        return i == len(name)