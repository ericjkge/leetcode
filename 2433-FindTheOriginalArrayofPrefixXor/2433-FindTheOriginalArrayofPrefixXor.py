# Last updated: 10/25/2025, 11:53:41 PM
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prefix = 0
        ans = [pref[0]]

        for i in range(1, len(pref)):
            ans.append(pref[i - 1] ^ pref[i])

        return ans