# Last updated: 7/12/2025, 3:25:07 PM
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        print(costs)
        total = counter = 0
        while counter < len(costs) and total + costs[counter] <= coins:
            total += costs[counter]
            counter += 1
            print(total, counter)
        return counter