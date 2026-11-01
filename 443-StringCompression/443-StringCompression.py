# Last updated: 11/1/2026, 11:20:00 AM
1class Solution:
2    def compress(self, chars: list[str]) -> int:
3        i = w = 0
4
5        while i < len(chars):            
6            j = i + 1
7            while j < len(chars) and chars[i] == chars[j]:
8                j += 1
9            count = j - i
10            chars[w] = chars[i]
11            w += 1
12            if count > 1:
13                for d in str(count):
14                    chars[w] = d
15                    w += 1
16            i = j
17        
18        return w