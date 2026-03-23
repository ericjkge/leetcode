# Last updated: 3/23/2026, 2:13:46 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordSet = set(wordDict)
4
5        @cache
6        def dp(i):
7            if i == len(s):
8                return True
9
10            for j in range(i, len(s) + 1):
11                if s[i:j] in wordSet and dp(j):
12                    return True
13            
14            return False
15        
16        return dp(0)