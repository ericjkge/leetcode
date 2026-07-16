# Last updated: 7/15/2026, 9:55:55 PM
1class Solution:
2    def longestStrChain(self, words: List[str]) -> int:
3        @cache
4        def dp(word):
5            longest = 1
6            for i in range(len(word)):
7                if word[:i] + word[i + 1:] in words:
8                    longest = max(longest, 1 + dp(word[:i] + word[i + 1:]))
9            return longest
10
11        return max(dp(words[i]) for i in range(len(words)))