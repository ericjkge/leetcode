# Last updated: 3/5/2026, 9:12:13 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        left = 0
4        right = len(s1)
5        s1_counter = Counter(s1)
6        s2_counter = Counter(s2[left:right])
7
8        if s1_counter == s2_counter:
9            return True
10
11        while right < len(s2):
12            s2_counter[s2[left]] -= 1
13            s2_counter[s2[right]] += 1
14
15            if s1_counter == s2_counter:
16                return True
17                
18            left += 1
19            right += 1
20        
21        return False