# Last updated: 7/9/2026, 8:41:36 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        p1 = p2 = 0
4        res = []
5
6        while p1 < len(word1) and p2 < len(word2):
7            res.append(word1[p1])
8            res.append(word2[p2])
9            p1 += 1
10            p2 += 1
11        
12        res.append(word1[p1:] if p1 < len(word1) else word2[p2:])
13        return "".join(res)