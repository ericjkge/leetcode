# Last updated: 1/30/2026, 10:35:25 AM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        start = 0
4        total = 0
5        tank = 0
6
7        for i in range(len(gas)):
8            change = gas[i] - cost[i]
9
10            total += change
11            tank += change
12            if tank < 0:
13                tank = 0
14                start = i + 1
15        
16        return start if total >= 0 else -1