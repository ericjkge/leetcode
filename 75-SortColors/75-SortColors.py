# Last updated: 6/29/2025, 4:19:52 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = Counter(nums)
        nums[:] = [0] * hashmap[0] + [1] * hashmap[1] + [2] * hashmap[2]
        
