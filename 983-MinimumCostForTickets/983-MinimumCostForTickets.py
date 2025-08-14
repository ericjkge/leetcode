# Last updated: 8/14/2025, 4:25:28 PM
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1] # last travel day
        travel = set(days) # travel days

        @cache
        def dp(i): # cheapest way to go from day i to last day
            if i > last:
                return 0
            
            if i not in travel: # can skip day i if not traveling, test next day
                return dp(i + 1)

            return min(
                costs[0] + dp(i + 1),
                costs[1] + dp(i + 7),
                costs[2] + dp(i + 30)
            )
        
        return dp(1)