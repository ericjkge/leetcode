# Last updated: 8/22/2025, 7:56:01 PM
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def dp(i): # answer for books[i:]
            if i == n:
                return 0
            
            best = float("inf")
            width = 0
            height = 0
            for j in range(i, n):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                best = min(best, height + dp(j + 1))
            return best

        return dp(0)