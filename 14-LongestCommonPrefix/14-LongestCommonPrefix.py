# Last updated: 12/9/2025, 11:24:22 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        strs.sort()
4        first, last = strs[0], strs[-1]
5        pointer = 0
6        prefix = []
7
8        while pointer < len(first) and pointer < len(last) and first[pointer] == last[pointer]:
9            prefix.append(first[pointer])
10            pointer += 1
11        
12        return "".join(prefix)
13
14        