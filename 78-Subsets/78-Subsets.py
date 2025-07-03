# Last updated: 7/3/2025, 1:10:38 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(index, path):
            ans.append(path[:])
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans
