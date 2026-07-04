# Last updated: 7/4/2026, 3:49:22 PM
1class Solution:
2    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
3        res = []
4        balls = defaultdict(int)
5        colors = defaultdict(list)
6
7        for x, y in queries:
8            if x in balls:
9                colors[balls[x]].remove(x)
10                if not colors[balls[x]]:
11                    del colors[balls[x]]
12
13            balls[x] = y
14            colors[y].append(x)
15            res.append(len(colors))
16
17        return res