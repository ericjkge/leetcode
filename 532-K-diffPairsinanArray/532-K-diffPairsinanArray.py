# Last updated: 7/4/2026, 2:14:56 PM
1class Solution:
2    def findPairs(self, nums: List[int], k: int) -> int:
3        freqs = Counter(nums)
4        count = 0
5
6        if k == 0:
7            return sum(1 for num in freqs if freqs[num] > 1)
8        else:
9            return sum(1 for num in freqs if num + k in freqs)
10
11        return count