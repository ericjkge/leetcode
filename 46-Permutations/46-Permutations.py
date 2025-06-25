# Last updated: 6/25/2025, 12:16:44 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(index + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans