# Last updated: 3/9/2026, 2:27:01 PM
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
14            if abs(px - x) != abs(py - y) or (x, y) == (px, py):
15                continue
16
17            total += self.points[(px, y)] * self.points[(x, py)] * freq
18        return total
19
20# Your DetectSquares object will be instantiated and called as such:
21# obj = DetectSquares()
22# obj.add(point)
23# param_2 = obj.count(point)