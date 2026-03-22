# Last updated: 3/22/2026, 9:22:04 AM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5
6        start = 0
7        tank = 0
8
9        for i in range(len(gas)):
10            tank += gas[i] - cost[i]
11
12            if tank < 0:
13                start = i + 1
14                tank = 0
15        
16        return start