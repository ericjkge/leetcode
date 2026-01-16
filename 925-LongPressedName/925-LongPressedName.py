# Last updated: 1/16/2026, 7:10:52 PM
1class Solution:
2    def isLongPressedName(self, name: str, typed: str) -> bool:
3        p1, p2 = 0, 0
4
5        if name[0] != typed[0]:
6            return False
7
8        while p1 < len(name) and p2 < len(typed):
9            if name[p1] == typed[p2]:
10                p1 += 1
11                p2 += 1
12            elif name[p1 - 1] == typed[p2]:
13                p2 += 1
14            else:
15                return False
16
17        while p2 < len(typed):
18            if typed[p2] == name[-1]:
19                p2 += 1
20            else:
21                return False
22        
23        if p1 < len(name):
24            return False
25
26        return True