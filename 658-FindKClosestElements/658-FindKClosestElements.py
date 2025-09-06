# Last updated: 9/6/2025, 2:12:01 PM
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        
        if arr[right] == x:
            closest = right
        else:
            closest = left
        
        ans = []
        n = len(arr)
        p1, p2 = closest, closest + 1
        while p1 >= 0 and p2 < n and len(ans) < k:
            c1 = arr[p1]
            c2 = arr[p2]
            if abs(c1 - x) <= abs(c2 - x):
                ans.append(c1)
                p1 -= 1
            else:
                ans.append(c2)
                p2 += 1
        
        if p1 >= 0:
            while len(ans) < k:
                ans.append(arr[p1])
                p1 -= 1
        else:
            while len(ans) < k:
                ans.append(arr[p2])
                p2 += 1

        return sorted(ans)