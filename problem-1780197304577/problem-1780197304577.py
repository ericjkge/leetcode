# Last updated: 5/30/2026, 8:15:04 PM
1class Solution:
2    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
3        freqs = Counter(nums)
4
5        for key, val in freqs.items():
6            if val > k:
7                freqs[key] = k
8
9        res = []
10        for key, val in freqs.items():
11            res.extend([key] * val)
12        return res