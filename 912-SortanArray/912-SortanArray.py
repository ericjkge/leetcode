# Last updated: 7/26/2025, 12:14:11 AM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def quickSort(start, end):
        #     if start >= end:
        #         return
        
        #     pivot = nums[(start + end) // 2]
        #     i, j = start, end
            
        #     while i <= j:
        #         while i <= j and nums[i] < pivot:
        #             i += 1
        #         while i <= j and nums[j] > pivot:
        #             j -= 1
                
        #         if i <= j:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j -= 1
            
        #     quickSort(start, j)
        #     quickSort(i, end)
        
        # quickSort(0, len(nums) - 1)

        return sorted(nums)