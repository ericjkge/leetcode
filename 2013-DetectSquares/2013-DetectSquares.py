# Last updated: 11/28/2025, 2:24:20 PM
1class DetectSquares:
2
3    def __init__(self):
4        self.points = defaultdict(int)
5
6    def add(self, point: List[int]) -> None:
7        self.points[(point[0], point[1])] += 1
8
9    def count(self, point: List[int]) -> int:
10        px, py = point
11        ans = 0
12
13        for (x, y), c1 in self.points.items():
14            if y != py or x == px:
15                continue
16
17            d = px - x
18
19            # coordinates of the two possible third corners
20            # 1) above square
21            p2 = (px, py + d)
22            p3 = (x,  py + d)
23
24            # 2) below square
25            p4 = (px, py - d)
26            p5 = (x,  py - d)
27
28            # count squares above
29            if p2 in self.points and p3 in self.points:
30                ans += c1 * self.points[p2] * self.points[p3]
31
32            # count squares below
33            if p4 in self.points and p5 in self.points:
34                ans += c1 * self.points[p4] * self.points[p5]
35
36        return ans
37
38# Your DetectSquares object will be instantiated and called as such:
39# obj = DetectSquares()
40# obj.add(point)
41# param_2 = obj.count(point)