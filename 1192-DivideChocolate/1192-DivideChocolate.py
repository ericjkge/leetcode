# Last updated: 5/30/2025, 12:07:35 PM
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        num = k + 1
        left = min(sweetness)
        right = sum(sweetness) // num
        
        while left < right:
            mid = (left + right + 1) // 2
            curr = 0
            counter = 0
            
            for s in sweetness:
                curr += s
                if curr >= mid:
                    curr = 0
                    counter += 1
            
            if counter >= num:
                left = mid
            else:
                right = mid -1
            
        return right