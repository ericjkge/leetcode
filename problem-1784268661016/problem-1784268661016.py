# Last updated: 7/16/2026, 11:11:01 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        lst = s.split()
4        return " ".join(lst[::-1])