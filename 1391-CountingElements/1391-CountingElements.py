# Last updated: 5/30/2025, 12:07:32 PM
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0
        for element in arr:
            if element + 1 in arr_set:
                count += 1
        return count