# Last updated: 8/21/2025, 9:12:13 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        def backtrack(path, index):
            ans.append(path[:])
            
            for i in range(index, n):
                if i == index or nums[i] != nums[i - 1]:
                    path.append(nums[i])
                    backtrack(path, i + 1)
                    path.pop()
        
        backtrack([], 0)
        return ans