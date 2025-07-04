# Last updated: 7/3/2025, 10:03:23 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        nonzeros = [] 
        for num in nums:
            if num != 0:
                nonzeros.append(num)
            else:
                zeros.append(num)
        nums[:] = nonzeros + zeros
        return nums