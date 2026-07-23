# Last updated: 7/22/2026, 8:54:00 PM
1class Solution:
2    def predictPartyVictory(self, senate: str) -> str:
3        n = len(senate)
4        radiants, dires = deque(), deque()
5
6        for i, c in enumerate(senate):
7            if c == "R":
8                radiants.append(i)
9            else:
10                dires.append(i)
11        
12        while radiants and dires:
13            if radiants[0] < dires[0]:
14                r = radiants.popleft()
15                radiants.append(r + n)
16                dires.popleft()
17            else:
18                d = dires.popleft()
19                dires.append(d + n)
20                radiants.popleft()
21        
22        if radiants:
23            return "Radiant"
24        return "Dire"