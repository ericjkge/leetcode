# Last updated: 7/19/2026, 10:15:33 AM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = "aeiou"
4        left = right = 0
5        window = 0
6        mx = 0
7
8        while right < len(s):
9            if s[right] in vowels:
10                window += 1
11            
12            if right < k - 1:
13                right += 1
14                continue
15
16            while right - left + 1 > k:
17                if s[left] in vowels:
18                    window -= 1
19                left += 1
20            
21            mx = max(mx, window)
22            right += 1
23        
24        return mx
25            
26