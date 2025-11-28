# Last updated: 11/28/2025, 2:28:15 PM
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
20            # Above
21            p2 = (px, py + side)
22            p3 = (x,  py + side)
23
24            # Below
25            p4 = (px, py - side)
26            p5 = (x,  py - side)
27
28            # Count above
29            if p2 in self.points and p3 in self.points:
30                ans += freq * self.points[p2] * self.points[p3]
31
32            # Count below
33            if p4 in self.points and p5 in self.points:
34                ans += freq * self.points[p4] * self.points[p5]
35
36        return ans
37
38# Your DetectSquares object will be instantiated and called as such:
39# obj = DetectSquares()
40# obj.add(point)
41# param_2 = obj.count(point)