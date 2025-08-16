# Last updated: 8/16/2025, 9:59:33 PM
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        @cache
        def inc(i, k):
            if k == 1:
                return 1
            curr = rating[i]
            total = 0
            for j in range(i + 1, n):
                if rating[j] > curr:
                    total += inc(j, k - 1)
            return total

        @cache
        def dec(i, k):
            if k == 1:
                return 1
            curr = rating[i]
            total = 0
            for j in range(i + 1, n):
                if rating[j] < curr:
                    total += dec(j, k - 1)
            return total


        ans = 0
        for i in range(n):
            ans += inc(i, 3) + dec(i, 3)
        
        return ans