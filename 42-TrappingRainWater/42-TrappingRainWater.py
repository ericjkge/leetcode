# Last updated: 11/11/2025, 9:47:23 AM
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mleft, mright = height[left], height[right]
        water = 0

        while left < right:
            if mleft <= mright:
                left += 1
                mleft = max(mleft, height[left])
                water += mleft - height[left]
            else:
                right -= 1
                mright = max(mright, height[right])
                water += mright - height[right]
        
        return water