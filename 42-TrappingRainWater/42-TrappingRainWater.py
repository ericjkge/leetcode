# Last updated: 9/24/2025, 9:43:34 AM
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mleft, mright = height[left], height[right]
        total = 0

        while left < right:
            if mleft < mright:
                left += 1
                mleft = max(mleft, height[left])
                total += mleft - height[left]
            else:
                right -= 1
                mright = max(mright, height[right])
                total += mright - height[right]
        
        return total