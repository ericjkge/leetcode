# Last updated: 3/7/2026, 11:07:37 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m, n = len(matrix), len(matrix[0])
4        left, right = 0, m * n - 1
5
6        while left + 1 < right:
7            mid = (left + right) // 2
8            r, c = mid // n, mid % n
9            if matrix[r][c] > target:
10                right = mid
11            else:
12                left = mid
13        
14        if matrix[left // n][left % n] == target or matrix[right // n][right % n] == target:
15            return True
16        return False
17        