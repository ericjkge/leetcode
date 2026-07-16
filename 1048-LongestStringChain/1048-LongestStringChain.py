# Last updated: 7/15/2026, 9:48:44 PM
1class Solution:
2    def longestStrChain(self, words: List[str]) -> int:
3        words.sort(key=lambda x: len(x))
4        seen = {}
5
6        @cache
7        def dp(i):
8            word = words[i]
9            longest = 1
10            for j in range(len(word)):
11                if word[:j] + word[j + 1:] in seen:
12                    longest = max(longest, 1 + dp(seen[word[:j] + word[j + 1:]]))
13            seen[word] = i
14            return longest
15        
16        return max(dp(i) for i in range(len(words)))