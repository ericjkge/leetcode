# Last updated: 8/20/2025, 10:23:58 PM
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        s = set(words) # O(1) look up

        @cache
        def dp(w):
            best = 1
            for i in range(len(w)):
                prev = w[:i] + w[i + 1:]
                if prev in s:
                    best = max(best, 1 + dp(prev))
            return best
        
        return max(dp(w) for w in s)
        