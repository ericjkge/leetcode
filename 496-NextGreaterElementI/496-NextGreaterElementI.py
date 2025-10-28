# Last updated: 10/28/2025, 9:55:21 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt = {}

        for num in nums2:
            while stack and stack[-1] < num:
                nxt[stack.pop()] = num
            stack.append(num)
        
        return [nxt.get(num, -1) for num in nums1]