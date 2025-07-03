# Last updated: 7/3/2025, 3:44:48 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mleft, mright = height[left], height[right]
        water = 0
        while left < right:
            if mleft <= mright:
                left += 1
                mleft = max(height[left], mleft)
                water += mleft - height[left]
            else:
                right -= 1
                mright = max(height[right], mright)
                water += mright - height[right]
        return water

