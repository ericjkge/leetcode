# Last updated: 7/4/2026, 2:03:27 PM
1class Solution:
2    def findPairs(self, nums: List[int], k: int) -> int:
3        freqs = Counter(nums)
4        count = 0
5
6        if k == 0:
7            for num in freqs:
8                if freqs[num] > 1:
9                    count += 1
10        else:
11            for num in freqs:
12                if num + k in freqs:
13                    count += 1
14
15        return count