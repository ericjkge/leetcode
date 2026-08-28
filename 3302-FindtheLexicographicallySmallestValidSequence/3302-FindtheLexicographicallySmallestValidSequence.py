# Last updated: 8/28/2026, 11:10:23 PM
1class Solution:
2    def validSequence(self, word1: str, word2: str) -> List[int]:
3        n, m = len(word1), len(word2)
4        last = [-1] * m
5        j = m - 1
6
7        for i in range(n - 1, -1 , -1):
8            if j >= 0 and word1[i] == word2[j]:
9                last[j] = i
10                j -= 1
11        
12        res = []
13        skip = j = 0
14        for i, c in enumerate(word1):
15            if j == m:
16                break
17            if c == word2[j] or skip == 0 and (j == m - 1 or i < last[j + 1]):
18                skip += c != word2[j]
19                res.append(i)
20                j += 1
21        
22        return res if j == m else []