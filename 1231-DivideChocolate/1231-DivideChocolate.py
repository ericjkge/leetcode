# Last updated: 9/21/2025, 12:43:55 AM
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canSplit(val):
            curr = 0
            pieces = 0
            for s in sweetness:
                curr += s
                if curr >= val:
                    pieces += 1
                    curr = 0
            return pieces >= k + 1

        left, right = 0, sum(sweetness) // (k + 1)

        while left + 1 < right:
            mid = (left + right) // 2
            if canSplit(mid):
                left = mid
            else:
                right = mid
        
        return right if canSplit(right) else left