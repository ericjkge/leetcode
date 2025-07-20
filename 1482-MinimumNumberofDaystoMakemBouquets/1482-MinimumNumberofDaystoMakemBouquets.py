# Last updated: 7/20/2025, 2:29:42 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def canMake(day):
            count = flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        count += 1
                        flowers = 0
                else:
                    flowers = 0
            return count >= m
        
        left, right = 0, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if canMake(mid):
                right = mid
            else:
                left = mid + 1
        return left