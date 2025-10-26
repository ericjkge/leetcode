# Last updated: 10/26/2025, 10:25:14 AM
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]

        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i - 1])
        
        return ans

    # XOR rule: a ^ b = c -> b = a ^ c  (pref[i] = pref[i - 1] ^ arr[i])