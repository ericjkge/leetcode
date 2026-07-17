# Last updated: 7/16/2026, 11:06:36 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = "aeiouAEIOU"
4        left, right = 0, len(s) - 1
5        s = list(s)
6
7        while left < right:
8            if s[left] in vowels and s[right] in vowels:
9                s[left], s[right] = s[right], s[left]
10                left += 1
11                right -= 1
12            elif s[left] in vowels:
13                right -= 1
14            elif s[right] in vowels:
15                left += 1
16            else:
17                left += 1
18                right -= 1
19        
20        return "".join(s)