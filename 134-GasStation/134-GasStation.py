# Last updated: 12/17/2025, 9:58:47 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n = len(gas)
4        start = 0
5        tank = 0
6        total = 0
7
8        for i in range(n):
9            change = gas[i] - cost[i]
10            tank += change
11            total += change
12
13            if tank < 0:
14                start = i + 1
15                tank = 0
16        
17        return start if total >= 0 else -1