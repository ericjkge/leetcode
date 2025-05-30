# Last updated: 5/30/2025, 12:07:51 PM
from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        ans = [-1] * len(nums1)
        
        hashmap = {n:i for i, n in enumerate(nums1)}
        
        for j in range(len(nums2)):
            while stack and nums2[j] > stack[-1]:
                ans[hashmap.get(stack.pop())] = nums2[j]
            if nums2[j] in hashmap.keys():
                stack.append(nums2[j])
        
        return ans