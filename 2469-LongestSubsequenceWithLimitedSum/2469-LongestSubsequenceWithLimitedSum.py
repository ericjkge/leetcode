# Last updated: 5/30/2025, 12:07:20 PM
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid + 1
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        ans = []
        for query in queries:            
            ans.append(binarySearch(prefix, query))
        return ans
            