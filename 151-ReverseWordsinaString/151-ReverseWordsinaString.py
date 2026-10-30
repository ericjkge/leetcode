# Last updated: 10/30/2026, 10:57:42 AM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        words = s.split()
4        return " ".join(words[::-1])