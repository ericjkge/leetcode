# Last updated: 6/27/2026, 4:18:30 PM
1class Solution:
2    def numPairsDivisibleBy60(self, time: List[int]) -> int:
3        mapping = defaultdict(int)
4        count = 0
5
6        for i in range(len(time)):
7            complement = (60 - time[i] % 60) % 60
8            if complement in mapping:
9                count += mapping[complement]
10            mapping[time[i] % 60] += 1
11
12        return count