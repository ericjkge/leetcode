# Last updated: 11/1/2026, 12:43:15 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        left = 0
4        vowels = "aeiou"
5        freqs = Counter()
6        ans = 0
7
8        for right in range(len(s)):
9            if s[right] in vowels:
10                freqs[s[right]] += 1
11            
12            if right < k - 1:
13                continue
14            else:
15                ans = max(ans, sum(freqs.values()))
16                if s[left] in vowels:
17                    freqs[s[left]] -= 1
18                left += 1
19        
20        return ans