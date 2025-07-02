# Last updated: 7/2/2025, 2:21:54 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dists.append((x ** 2 + y ** 2, (x, y)))
        
        dists.sort()
        ans = []
        for i in range(k):
            ans.append(dists[i][1])
        return ans
