# Last updated: 8/5/2025, 11:51:24 PM
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])

        def hasPixelCol(col):
            return any(image[r][col] == "1" for r in range(rows))

        def hasPixelRow(row):
            return any(image[row][c] == "1" for c in range(cols))

        # Find left
        lo, hi = 0, y
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if hasPixelCol(mid):
                hi = mid
            else:
                lo = mid
        if hasPixelCol(lo):
            left = lo
        else:
            left = hi

        # Find right
        lo, hi = y, cols - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if hasPixelCol(mid):
                lo = mid
            else:
                hi = mid
        if hasPixelCol(hi):
            right = hi
        else:
            right = lo
        
        # Find top
        lo, hi = 0, x
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if hasPixelRow(mid):
                hi = mid
            else:
                lo = mid
        if hasPixelRow(lo):
            top = lo
        else:
            top = hi
        
        # Find bottom
        lo, hi = x, rows - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if hasPixelRow(mid):
                lo = mid
            else:
                hi = mid
        if hasPixelRow(hi):
            bottom = hi
        else:
            bottom = lo

        return (right - left + 1) * (bottom - top + 1)