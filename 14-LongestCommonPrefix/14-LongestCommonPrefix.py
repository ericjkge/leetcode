# Last updated: 12/9/2025, 11:26:31 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        prefix = strs[0]
4        for i in range(1, len(strs)):
5            pointer = 0
6            new_prefix = []
7            while pointer < min(len(prefix), len(strs[i])) and prefix[pointer] == strs[i][pointer]:
8                new_prefix.append(prefix[pointer])
9                pointer += 1
10            prefix = "".join(new_prefix)
11
12        return prefix
13
14        