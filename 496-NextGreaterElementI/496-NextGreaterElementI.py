# Last updated: 10/24/2025, 10:41:09 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                nxt[stack.pop()] = num
            stack.append(num)
        
        return [nxt.get(num, -1) for num in nums1]