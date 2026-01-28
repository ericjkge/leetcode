# Last updated: 1/28/2026, 9:06:35 AM
1class DetectSquares:
2
3    def __init__(self):        
4        self.points = Counter()
5
6    def add(self, point: List[int]) -> None:
7        self.points[tuple(point)] += 1
8
9    def count(self, point: List[int]) -> int:
10        total = 0
11        px, py = point
12
13        for (x, y), freq in self.points.items():
14            if abs(x - px) == abs(y - py) and x != px:
15                total += freq * self.points[(x, py)] * self.points[(px, y)]
16
17        return total
18
19
20# Your DetectSquares object will be instantiated and called as such:
21# obj = DetectSquares()
22# obj.add(point)
23# param_2 = obj.count(point)