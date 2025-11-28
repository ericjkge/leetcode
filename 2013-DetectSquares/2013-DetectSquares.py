# Last updated: 11/28/2025, 2:34:37 PM
1class DetectSquares:
2
3    def __init__(self):
4        self.points = defaultdict(int)
5
6    def add(self, point: List[int]) -> None:
7        x, y = point
8        self.points[(x, y)] += 1
9
10    def count(self, point: List[int]) -> int:
11        px, py = point
12        ans = 0
13
14        for (x, y), freq in self.points.items():
15            if y != py or x == px:
16                continue
17
18            side = px - x
19
20            # Check above
21            ans += freq * self.points.get((px, py + side), 0) * self.points.get((x,  py + side), 0)
22
23            # Check below
24            ans += freq * self.points.get((px, py - side), 0) * self.points.get((x,  py - side), 0)
25
26        return ans
27
28# Your DetectSquares object will be instantiated and called as such:
29# obj = DetectSquares()
30# obj.add(point)
31# param_2 = obj.count(point)