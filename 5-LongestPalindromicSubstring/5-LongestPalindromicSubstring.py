# Last updated: 9/6/2025, 1:33:24 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1
        
        for k in range(n):
            even_len = expand(k, k + 1)
            dist = even_len // 2
            even = s[k - dist + 1:k + dist + 1]
            if len(even) > len(ans):
                ans = even
            odd_len = expand(k, k)
            dist = odd_len // 2
            odd = s[k - dist:k + dist + 1]
            if len(odd) > len(ans):
                ans = odd
        
        return ans
