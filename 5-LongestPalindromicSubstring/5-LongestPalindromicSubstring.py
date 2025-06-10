# Last updated: 6/9/2025, 11:45:10 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1
        
        ans = [0, 0]
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]
            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = even_length // 2 - 1
                ans = [i - dist, i + 1 + dist]
        
        return s[ans[0]:ans[1] + 1]
