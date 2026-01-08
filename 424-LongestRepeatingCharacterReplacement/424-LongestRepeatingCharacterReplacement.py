# Last updated: 1/8/2026, 11:02:03 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left = 0
4        freqs = {}
5        max_f = 0
6        longest = 0
7
8        for right in range(len(s)):
9            # Update frequency and current max frequency
10            freqs[s[right]] = freqs.get(s[right], 0) + 1
11            max_f = max(max_f, freqs[s[right]])
12
13            # Window is invalid if: (window size - max_f) > k
14            # We only need to shift the left pointer once (if) 
15            # because we only care about expanding the maximum window found so far.
16            if (right - left + 1) - max_f > k:
17                freqs[s[left]] -= 1
18                left += 1
19            
20            longest = right - left + 1
21            
22        return longest