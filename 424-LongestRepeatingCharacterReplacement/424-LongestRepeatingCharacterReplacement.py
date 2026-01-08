# Last updated: 1/8/2026, 10:59:23 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left, right = 0, 0
4        longest = 0
5        freqs = defaultdict(int)
6
7        while right < len(s):
8            freqs[s[right]] += 1
9            while sum(freqs.values()) - max(freqs.values()) > k:
10                letter = s[left]
11                freqs[letter] -= 1
12                if freqs[letter] == 0:
13                    del freqs[letter]
14                left += 1
15            longest = max(longest, right - left + 1)
16            right += 1
17        
18        return longest
19
20
21        return longest