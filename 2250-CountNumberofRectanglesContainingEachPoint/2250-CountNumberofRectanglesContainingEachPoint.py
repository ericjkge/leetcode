# Last updated: 7/18/2025, 11:52:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        ans = [[-1, -1] for _ in range(len(queries))]
        
        def binarySearchMin(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1 if left > 0 else -1

        def binarySearchMax(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left if left < len(arr) else -1

        for i in range(len(queries)):
            mini = binarySearchMin(arr, queries[i])
            maxi = binarySearchMax(arr, queries[i])
            ans[i][0] = arr[mini] if mini != -1 else -1
            ans[i][1] = arr[maxi] if maxi != -1 else -1

        return ans