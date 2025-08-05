# Last updated: 8/6/2025, 12:35:26 AM
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mleft, mright = height[left], height[right]
        water = 0
        while left < right:
            if mleft <= mright:
                left += 1
                mleft = max(height[left], mleft)
                water += mleft - height[left] # Note: do mleft instead of min(mleft, mright) here,
                # since this way it self-corrects to 0 but min could give negative
            else:
                right -= 1
                mright = max(height[right], mright)
                water += mright - height[right]
        return water

