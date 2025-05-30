# Last updated: 5/30/2025, 12:07:47 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewels_set = set(jewels)
        for char in stones:
            if char in jewels_set:
                counter +=1
        return counter