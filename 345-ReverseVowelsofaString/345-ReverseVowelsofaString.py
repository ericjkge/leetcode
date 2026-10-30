# Last updated: 10/30/2026, 10:51:15 AM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        s_list = list(s)
4        i, j = 0, len(s) - 1
5        vowels = {"a", "e", "i", "o", "u"}
6
7        while i < j:
8            if s_list[i].lower() in vowels and s_list[j].lower() in vowels:
9                s_list[i], s_list[j] = s_list[j], s_list[i]
10                i += 1
11                j -= 1
12            elif s_list[i].lower() in vowels:
13                j -= 1
14            elif s_list[j].lower() in vowels:
15                i += 1
16            else:
17                i += 1
18                j -= 1
19        
20        return "".join(s_list)
21